# DropboxSQL

This is a Python script that allows you to create backups of your MySQL/MariaDB databases and upload them to your Dropbox account.

## Prerequisites

1. Python 3.x installed on your system.
```bash
sudo apt install python3
```
2. A Dropbox account with an access token. To create an access token, follow the [official Dropbox documentation](https://www.dropbox.com/developers/reference/oauth-guide).


    # Create a Dropbox App with Write Permissions

    This guide will show you how to create a Dropbox app and give it write permissions.

    ## Prerequisites

    1. A Dropbox account. If you don't have one, sign up at [https://www.dropbox.com](https://www.dropbox.com).

    ## Steps

    1. Visit the Dropbox App Console at [https://www.dropbox.com/developers/apps/create](https://www.dropbox.com/developers/apps/create).

    2. Select the type of access your app will need:
       - **Scoped access**: Choose this option for more granular control over app permissions.
       - **Full dropbox**: Choose this option if your app needs access to all files and folders in your Dropbox.

    3. Enter a unique name for your app in the "App name" field.

    4. Click the "Create App" button.

    5. Once your app is created, you'll be redirected to the app's settings page. Here, you can manage your app's settings and permissions.

    6. In the "OAuth 2" section, click the "Generate" button to create an access token. This token will be used to authenticate your app with Dropbox. Make sure to keep this token secure, as it grants access to your Dropbox account.

    7. To set write permissions, go to the "Permissions" tab on the app's settings page.

    8. Scroll through the list of permissions and enable the ones your app requires for writing. For example, if your app needs to write files and folders, enable the `files.metadata.write`, `files.content.write`, and `files.metadata.read` permissions.

    9. Click the "Submit" button at the bottom of the page to save your changes.

    Your Dropbox app is now set up with write permissions. Use the generated access token to authenticate with the Dropbox API in your application.



3. MySQL or MariaDB installed on your system.


## Setup

1. Clone the repository or download the script:

    ```bash
    git clone https://github.com/MrZaKaRiA/DropboxSQL.git
    ```

2. Install the `dropbox` package using pip:

    ```bash
    pip install dropbox
    ```

3. Open the script and replace the following placeholders with your own credentials:

    ```python
    db_user = 'your_db_user'
    db_password = 'your_db_password'
    dropbox_access_token = 'your_dropbox_access_token'
    ```

4. (Optional) Adjust the `backup_dir` variable if you want to use a different directory for temporary backup files:

    ```python
    backup_dir = '/tmp'
    ```

## Usage

To make the script executable, you can run the following command in your terminal:

```bash
chmod +x mysql_backup_to_dropbox.py
```

After you've made the script executable, you can run it directly:

```bash
./mysql_backup_to_dropbox.py
```

Please note that you need to be in the same directory as the script to run the commands above. If the script is in a different directory, provide the full path to the script:

```bash
chmod +x /path/to/mysql_backup_to_dropbox.py
```

The script will create a backup of each database (excluding information_schema and performance_schema) and upload it to a folder in your Dropbox account. The folder structure in Dropbox will be /sql_backups/YYYY-MM-DD-HH:MM:SS/.

Each backup file will be named {database}.sql.



# Schedule Script at Midnight

This guide will show you how to schedule a script to run at midnight using `crontab` on Linux.

## Prerequisites

1. A Linux system with `crontab` installed.
2. A script you want to run at midnight.

## Steps


1. Type `crontab -e` on terminal to open the cron table for editing. If this is the first time you're running this command, it may prompt you to choose an editor (e.g., nano, vim, etc.). Choose the one you're comfortable with.

2. Add the following line at the end of the file:

    ```
    0 0 * * * /path/to/your/script
    ```

    Replace `/path/to/your/script` with the full path to the script you want to execute.

    This line means that the script will run at `0` minutes and `0` hours (midnight) every day of the month, every month, and every day of the week.

3. Save the file and exit the editor. The cron job is now scheduled.




Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
