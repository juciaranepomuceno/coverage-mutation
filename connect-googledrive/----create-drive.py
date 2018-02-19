from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

# file1 = drive.CreateFile({'title': 'Hello',
#                        'mimeType': 'application/vnd.google-apps.spreadsheet'})


# file1.SetContentString('Hello World!') # Set content of the file from given string.
# file1.Upload()


file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file1 in file_list:
    print('title: %s, id: %s mime: %s' % (file1['title'], file1['id'], file1['mimeType']))
