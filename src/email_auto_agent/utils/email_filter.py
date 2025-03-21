import os
import base64
from email.mime.text import MIMEText
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage, HumanMessage
from email_auto_agent.utils.gmail_service import authenticate_gmail

load_dotenv()
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("MODEL")

#initialize Gmail API
gmail_service = authenticate_gmail()

#Initialize Langchain Model
llm = ChatGoogleGenerativeAI(model = MODEL, api_key=GOOGLE_API_KEY)

class EmailFilterCrew:
    """Handles fetching emails and generating draft responses"""
    
    #FETCH GMAIL EMAILS
    def fetch_gmail_emails(self, max_results =1):
        print("****In fetch Email:")
        results = gmail_service.users().messages().list(
            userId = "me", maxResults = max_results, labelIds = ["INBOX"]
        ).execute()
        messages = results.get("messages",[])
        emails = []
    
        for msg in messages:
            msg_id = msg["id"]
            msg_data = gmail_service.users().messages().get(userId = "me", id = msg_id).execute()
            email = {
                "id": msg_id,
                "sender": next(
                    header["value"]
                    for header in msg_data["payload"]["headers"]
                    if header["name"] == "From"
                ),
                "subject": next(
                    header["value"]
                    for header in msg_data["payload"]["headers"]
                    if header["name"] == "Subject"
                ),
                "body":self.extract_email_body(msg_data)
            }
            emails.append(email)
        return emails

    def extract_email_body(self, msg_data):
        print("****In Extract Email Body")
        """Extract the email body from Gmail API response"""
        try:
            if "parts" in msg_data["payload"]:
                for part in msg_data["payload"]["parts"]:
                    if part["mimeType"] == "text/plain":
                        return base64.urlsafe_b64decode(part["payload"]["body"]["data"]).decode("utf-8")
            return base64.urlsafe_b64decode(msg_data["payload"]["body"]["data"]).decode("utf-8")
        except Exception:
            return "Unable to extract email body"

    #RESPONSE GENERATOR
    def generate_response(self,email):
        print("****In Generate Response")
        """Uses LangChain to generate a draft response"""
        
        prompt = [
            SystemMessage(content = "You are an AI Assistant that generates professional email replies."),
            HumanMessage(content = f""" Email received from {email['sender']} with subject '{email['subject']}:{email['body']}.
            Generate a polite response.
            only return the response text without any preamble or your suggestions. At the end of the response write formal greetings
                                    """)
        ]
        response = llm(prompt)
        return prompt.content

    #Save Draft to GMAIL
    def save_draft_to_gmail(self, recipient, subject,body):
        """Saves an AI generated email as a draft in Gmail"""
        print("****In Save Draft to Gamil")
        message = MIMEText(body)
        message["to"]= recipient
        message["subject"] = f"Re. {subject}"
        raw_message = base64.urlsafe_b64encode(message.as_byte()).decode("utf-8")
        draft = {"message": {"raw": raw_message}}
        
        try:
            draft_response = gmail_service.users().drafts().create(userId="me", body=draft).execute()
            print ("Email Filter: Save Draft Done")
            return draft_response
        except Exception as e:
            return f"Error saving draft"