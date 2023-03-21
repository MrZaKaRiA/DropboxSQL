# DropboxSQL

This is a Python script that allows you to create backups of your MySQL/MariaDB databases and upload them to your Dropbox account.

##Prerequisites

Python 3.x installed on your system.
A Dropbox account with an access token. To create an access token, follow the official Dropbox documentation.
MySQL or MariaDB installed on your system.
Setup

Clone the repository or download the script:

<pre>
```bash
git clone https://github.com/MrZaKaRiA/DropboxSQL.git
</pre>

Install the dropbox package using pip:
<pre>
```bash
pip install dropbox
</pre>

Open the script and replace the following placeholders with your own credentials:

<pre>
```python

db_user = 'your_db_user'
db_password = 'your_db_password'
dropbox_access_token = 'your_dropbox_access_token'
</pre>

(Optional) Adjust the backup_dir variable if you want to use a different directory for temporary backup files:
<pre>
```python

backup_dir = '/tmp'
</pre>

##Usage

To make the script executable, you can run the following command in your terminal:

<pre>
```bash
chmod +x mysql_backup_to_dropbox.py
</pre>

After you've made the script executable, you can run it directly:

<pre>
```bash
./mysql_backup_to_dropbox.py
</pre>

Please note that you need to be in the same directory as the script to run the commands above. If the script is in a different directory, provide the full path to the script:

<pre>
```bash

chmod +x /path/to/mysql_backup_to_dropbox.py
</pre>

The script will create a backup of each database (excluding information_schema and performance_schema) and upload it to a folder in your Dropbox account. The folder structure in Dropbox will be /sql_backups/YYYY-MM-DD-HH:MM:SS/.

Each backup file will be named {database}.sql.

##Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
