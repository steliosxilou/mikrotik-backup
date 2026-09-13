import os
import time
import paramiko

router_ip = "your router IP"
username = "username of the user on the router"
password = os.environ["MIKROTIK_PASSWORD"]
backup_name = "choose a backup name"

backup_command = f"/system backup save name={backup_name}"

local_folder = os.path.join(os.environ["USERPROFILE"], "Documents")
local_filepath = os.path.join(local_folder, f"{backup_name}.backup")
remote_filepath = f"/{backup_name}.backup"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    print("Connection to router...")

    ssh.connect(
        router_ip,
        username=username,
        password=password,
        timeout=15
    )

    print("Creating Backup to router...")

    stdin, stdout, stderr = ssh.exec_command(backup_command)
    error = stderr.read().decode().strip()

    if error:
        raise RuntimeError(f"Error RouterOS: {error}")

    time.sleep(5)

    print("Open SFTP to download backup...")

    sftp = ssh.open_sftp()

    try:
        file_info = sftp.stat(remote_filepath)

        if file_info.st_size > 0:
            sftp.get(remote_filepath, local_filepath)
            print(f"Backup saved to: {local_filepath}")
        else:
            print("Backup file is empty. Download cancelled.")

    finally:
        sftp.close()

except Exception as e:
    print(f"Failed: {e}")

finally:
    ssh.close()
