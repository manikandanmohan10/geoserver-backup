from pydrive2.auth import GoogleAuth
from pydrive2.auth import ServiceAccountCredentials
from pydrive2.drive import GoogleDrive
import os

def authenticate():
    scope = ['https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('service_account.json', scope)
    gauth = GoogleAuth()
    gauth.credentials = creds
    drive = GoogleDrive(gauth)
    return drive


def upload_file(drive, local_file_path, folder_id=None):
    try:
        file_name = os.path.basename(local_file_path)
        gfile = drive.CreateFile({'title': file_name, 'parents': [{'id': folder_id}] if folder_id else []})
        gfile.SetContentFile(local_file_path)
        gfile.Upload()
        print(f"Uploaded: {file_name}")
    except Exception as e:
        print(f"Error uploading {file_name}: {e}")

def main():
    drive = authenticate()
    folder_id = '1LM_fb457gfkw13JClBzco4ZNvibCWHsA'
    backup_dir = 'backup'
    for root, _, files in os.walk(backup_dir):
        for file in files:
            file_path = os.path.join(root, file)
            upload_file(drive, file_path, folder_id)

if __name__ == "__main__":
    main()
