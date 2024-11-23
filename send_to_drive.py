from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import json

#TODO: remake cvs to json

def upload():
    gauth = GoogleAuth()

    try:
        with open("client-data/client_secrets.json", "r") as file:
            data = json.load(file)
        if 'web' not in data or 'client_id' not in data['web']:
            raise ValueError("File client_secrets.json has the wrong format.")
    except FileNotFoundError:
        print("File client_secrets.json not found!")
        return
    except ValueError as e:
        print(f"Error: {e}")
        return

    if os.path.exists("client-data/credentials.json"):
        gauth.LoadCredentialsFile("credentials.json")
        if gauth.access_token_expired:
            gauth.Refresh()
        else:
            gauth.Authorize()
    else:
        gauth.LocalWebserverAuth()
        gauth.SaveCredentialsFile("credentials.json")

    drive = GoogleDrive(gauth)

    folder_path = 'datasets'
    if not os.path.exists(folder_path):
        print(f"Folder {folder_path} was not found.")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            print(f"Uploading a file: {filename}")
            file_drive = drive.CreateFile({'title': filename})
            file_drive.SetContentFile(file_path)
            file_drive.Upload()
            print(f"File {filename} was successfully uploaded to Google Drive!")

if __name__ == '__main__':
    upload()
