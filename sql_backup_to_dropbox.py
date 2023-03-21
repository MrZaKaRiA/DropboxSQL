#!/usr/bin/env python3
import os
import subprocess
import sys
import time
from dropbox import Dropbox, files

# Replace with your own MySQL/MariaDB credentials
db_user = 'your_db_user'
db_password = 'your_db_password'

# Replace with your own Dropbox API access token
dropbox_access_token = 'your_dropbox_access_token'

# Set the backup directory
backup_dir = '/tmp'

def get_databases():
    command = f'mysql --user={db_user} --password={db_password} --skip-column-names -e "SHOW DATABASES;"'
    databases = subprocess.check_output(command, shell=True).decode('utf-8').strip().split('\n')
    # Exclude information_schema and performance_schema
    databases = [db for db in databases if db not in ('information_schema', 'performance_schema')]
    return databases

def create_backup(database, backup_file_path):
    command = f'mysqldump --user={db_user} --password={db_password} --databases {database} --result-file={backup_file_path} --single-transaction --skip-lock-tables'
    subprocess.check_call(command, shell=True)

def upload_to_dropbox(dropbox_access_token, backup_file_path, remote_file_path):
    dbx = Dropbox(dropbox_access_token)
    with open(backup_file_path, 'rb') as f:
        dbx.files_upload(f.read(), remote_file_path, mode=files.WriteMode('overwrite'))

def main():
    databases = get_databases()
    timestamp = time.strftime('%Y%m%d%H%M%S')

    # Create timestamp folder in the backup directory
    timestamp_folder = os.path.join(backup_dir, timestamp)
    os.makedirs(timestamp_folder)

    for database in databases:
        backup_file = f'{database}.sql'
        backup_file_path = os.path.join(timestamp_folder, backup_file)
        remote_file_path = f'/sql_backups/{timestamp}/{backup_file}'

        create_backup(database, backup_file_path)
        upload_to_dropbox(dropbox_access_token, backup_file_path, remote_file_path)
        os.remove(backup_file_path)

    os.rmdir(timestamp_folder)

if __name__ == '__main__':
    main()
