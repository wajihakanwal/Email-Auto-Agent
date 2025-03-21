from crewai.tools import tool
from email_auto_agent.utils.email_filter import EmailFilterCrew

@tool("fetch email tool")
def fetch_email_tool() -> dict:
    """fetch emails from given email id

    Returns:
        dict: contains the recipient, subject, and body of the email
    """
    #Create an instance of EmailFilterCrew
    email_filter_crew = EmailFilterCrew()
    #Fetch the Gmail emails
    emails = email_filter_crew.fetch_gmail_emails()
    email = emails[0]
    return(email)


@tool("response_tool")
def response_email_tool(email:dict) -> dict:
    """Generate a response for the given email.

    Args:
        email (dict): Contains the sender, subject, and the body of the email.

    Returns:
        dict: Contains the recipient and the response to the email
    """
    email_filter_crew = EmailFilterCrew()
    draft_response = email_filter_crew.generate_response(email)
    email_filter_crew.save_draft_to_gmail(email["sender"],email["subject"], draft_response)
    return draft_response