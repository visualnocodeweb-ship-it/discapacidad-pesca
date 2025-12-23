import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.readonly',
    'https://www.googleapis.com/auth/gmail.send'
]
TOKEN_PATH = 'token.json'
CREDS_PATH = 'credentials.json'

def main():
    if os.path.exists(TOKEN_PATH):
        print(f"'{TOKEN_PATH}' ya existe. Elimínalo para generar uno nuevo.")
        return
    if not os.path.exists(CREDS_PATH):
        print(f"Error: No se encuentra '{CREDS_PATH}'.")
        return
    
    flow = InstalledAppFlow.from_client_secrets_file(CREDS_PATH, SCOPES)
    creds = flow.run_local_server(port=0)
    
    with open(TOKEN_PATH, 'w') as token:
        token.write(creds.to_json())
        print(f"\n¡Token guardado en '{TOKEN_PATH}'!")

if __name__ == '__main__':
    main()

