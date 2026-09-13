import os
import time
import paramiko

router_ip = "192.168.10.1"
username = "admin"
password = os.environ["MIKROTIK_PASSWORD"]
backup_name = "Weekly_10_1_backup"

backup_command = f"/system backup save name={backup_name}"

local_folder = os.path.join(os.environ["USERPROFILE"], "Documents")
local_filepath = os.path.join(local_folder, f"{backup_name}.backup")
remote_filepath = f"/{backup_name}.backup"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    print("Σύνδεση στο router...")

    ssh.connect(
        router_ip,
        username=username,
        password=password,
        timeout=15
    )

    print("Δημιουργία backup στο router...")

    stdin, stdout, stderr = ssh.exec_command(backup_command)
    error = stderr.read().decode().strip()

    if error:
        raise RuntimeError(f"Σφάλμα RouterOS: {error}")

    time.sleep(5)

    print("Άνοιγμα SFTP για λήψη του backup...")

    sftp = ssh.open_sftp()

    try:
        file_info = sftp.stat(remote_filepath)

        if file_info.st_size > 0:
            sftp.get(remote_filepath, local_filepath)
            print(f"Το backup αποθηκεύτηκε στο: {local_filepath}")
        else:
            print("Το αρχείο backup είναι άδειο. Η λήψη ακυρώθηκε.")

    finally:
        sftp.close()

except Exception as e:
    print(f"Αποτυχία: {e}")

finally:
    ssh.close()