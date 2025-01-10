from pydrive2.auth import GoogleAuth
from pydrive2.auth import ServiceAccountCredentials
from pydrive2.drive import GoogleDrive
import os
from datetime import datetime
import shutil

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


def create_folder(drive, folder_name, parent_id=None):
    try:
        folder_metadata = {
            'title': folder_name,
            'mimeType': 'application/vnd.google-apps.folder',
            'parents': [{'id': parent_id}] if parent_id else []
        }
        folder = drive.CreateFile(folder_metadata)
        folder.Upload()
        print(f"Folder created: {folder_name} (ID: {folder['id']})")
        return folder['id']
    except Exception as e:
        print(f"Error creating folder {folder_name}: {e}")
        return None
    

def main():
    drive = authenticate()
    folder_id = '1LM_fb457gfkw13JClBzco4ZNvibCWHsA'
    file_name = datetime.now().date().strftime('%Y-%m-%d')
    shutil.make_archive('temp_drive_backup/'+file_name+'.zip', 'zip', f"db/{file_name}")
    shutil.make_archive('temp_drive_backup/geoserver_upload_datas.zip', 'zip', "geoserver_upload_datas")
    subfolder_id = create_folder(drive, file_name, parent_id=folder_id)
    backup(drive, 'temp_drive_backup', subfolder_id)
    shutil.rmtree('temp_drive_backup')

def backup(drive, folder_name, folder_id):
    
    backup_dir = folder_name
    for root, _, files in os.walk(backup_dir):
        for file in files:
            file_path = os.path.join(root, file)
            upload_file(drive, file_path, folder_id)

if __name__ == "__main__":
    main()
