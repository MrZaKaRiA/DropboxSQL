# DropboxSQL

This is a Python script that allows you to create backups of your MySQL/MariaDB databases and upload them to your Dropbox account.

## Prerequisites

1. Python 3.x installed on your system.
```bash
sudo apt install python3
```
2. A Dropbox account with an access token. To create an access token, follow the [official Dropbox documentation](https://www.dropbox.com/developers/reference/oauth-guide).

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
