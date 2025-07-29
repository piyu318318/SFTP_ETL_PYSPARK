from datetime import datetime
import pysftp
from io import BytesIO
import pandas as pd



hostname = "192.168.1.33"
username = "sftpuser"
password = "StrongPassword@123"
remote_path = "/loan_data_1.csv"

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

with pysftp.Connection(host=hostname, username=username, password=password, cnopts=cnopts) as sftp:
    print(f"Connected to {hostname}")

    with sftp.open(remote_path, mode='rb') as remote_file:
        buffer = BytesIO(remote_file.read())

    df = pd.read_csv(buffer)



    print("CSV data loaded into memory:")

    df['loan_amount'] = df['loan_amount'].fillna(0)
    df['emi'] = df['emi'].fillna(0)
    df['start_date'] = pd.to_datetime(df['start_date']).dt.date
    df['end_date'] = pd.to_datetime(df['end_date']).dt.date
    df['status'] = df['status'].str.strip().str.lower()

    print(df.head())
