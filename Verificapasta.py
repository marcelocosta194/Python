import os

folder_path = 'c:\pythonfolder'
if not os.path.exists(folder_path):
    os.mkdir(folder_path)
    print(f"Folder '{folder_path}' created.")
else:
    print(f"Folder '{folder_path}' already exists.")
    os.rmdir(folder_path)