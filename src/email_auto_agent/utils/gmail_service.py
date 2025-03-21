import os
from google.auth.transport.requests import  Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.discovery import Resource
from typing import cast
#OAuth 2.0 Scopes for Gmail API

'''SCOPES = [
    "https://www.googleapi.com/auth/gmail.modify",
    "https://www.googleapi.com/auth/gmail.compose",
    "https://www.googleapi.com/auth/gmail.readonly"
]'''
SCOPES = ["https://mail.google.com/"]
SCOPES = [
    "https://www.googleapi.com/auth/gmail.modify",
    "https://www.googleapi.com/auth/gmail.compose",
    "https://www.googleapi.com/auth/gmail.readonly"
]

def authenticate_gmail():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json",SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json",SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json","w") as token:
            token.write(creds.to_json())
    print ("Gmail service: Authentication Done")
    return cast(Resource, build("gmail","v1",credentials=creds))
