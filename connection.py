import pysftp

hostname = "192.168.1.35"
username = "sftpuser"
password = "StrongPassword@123"
remote_path = "/"
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

with pysftp.Connection(host=hostname, username=username, password=password, cnopts=cnopts) as sftp:
    print(f"Connected to {hostname}")

    # List files in the remote directory
    file_list = sftp.listdir(remote_path)

    print("Files in remote folder:")
    for file in file_list:
        print(file)



