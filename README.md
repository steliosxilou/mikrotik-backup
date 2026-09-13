\# MikroTik Backup Script



\[Ελληνική έκδοση / Greek version](README\_GR.md)



A Python script that creates a MikroTik RouterOS binary backup and downloads it to the Windows Documents folder.



\## What it does



1\. Connects to the MikroTik router through SSH.

2\. Creates a RouterOS binary `.backup` file.

3\. Waits for the backup file to be created.

4\. Opens an SFTP channel through the existing SSH connection.

5\. Downloads the backup to the current Windows user's Documents folder.

6\. Closes the SFTP and SSH connections.



\## Requirements



\- Windows

\- Python 3

\- Network access to the MikroTik router

\- SSH and SFTP enabled on the MikroTik router

\- The `paramiko` Python package



\## Installation



Install Paramiko from PowerShell:



```powershell

py -m pip install paramiko

```



\## Password configuration



The router password is not stored in the Python script.



Set it once as a Windows environment variable:



```powershell

setx MIKROTIK\_PASSWORD "your-router-password"

```



Close and reopen PowerShell or your terminal after running this command.



> Never commit router passwords to GitHub.



\## Script configuration



Update these values in `mikrotik-backup.py` when necessary:



```python

router\_ip = "192.168.10.1"

username = "admin"

backup\_name = "Weekly\_10\_1\_backup"

```



\## Run the script



From the project folder:



```powershell

py mikrotik-backup.py

```



The backup is saved in:



```text

C:\\Users\\YOUR\_WINDOWS\_USERNAME\\Documents

```



\## Scheduled execution



Use Windows Task Scheduler to run the script automatically on a specific date and time.



\- \*\*Program/script:\*\* path to `python.exe`

\- \*\*Add arguments:\*\* full path to `mikrotik-backup.py`



\## Security



\- Do not store passwords in the Python file.

\- Do not upload `.backup` files to GitHub.

\- RouterOS binary backups may contain sensitive configuration data.

\- This repository ignores `.backup` and environment files through `.gitignore`.

