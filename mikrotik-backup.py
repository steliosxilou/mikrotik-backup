import os
import time
import paramiko

router_ip = "YOUR_ROUTER_IP"
username = "YOUR_ROUTER_USERNAME"
password = os.environ["MIKROTIK_PASSWORD"]
backup_name = "YOUR_BACKUP_NAME"

backup_command = f"/system backup save name={backup_name}"

local_folder = os.path.join(os.environ["USERPROFILE"], "Documents")
local_filepath = os.path.join(local_folder, f"{backup_name}.backup")
remote_filepath = f"/{backup_name}.backup"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    print("Connecting to router...")

    ssh.connect(
        router_ip,
        username=username,
        password=password,
        timeout=15
    )

    print("Creating backup on router...")

    stdin, stdout, stderr = ssh.exec_command(backup_command)
    error = stderr.read().decode().strip()

    if error:
        raise RuntimeError(f"RouterOS error: {error}")

    time.sleep(5)

    print("Opening SFTP connection to download backup...")

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