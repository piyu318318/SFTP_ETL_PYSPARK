import pysftp
from io import BytesIO
import pandas as pd
from sqlalchemy import create_engine

hostname = "192.168.1.34"
username = "sftpuser"
password = "StrongPassword@123"
remote_path = "/"


mysql_user = 'root'
mysql_password = 'root123'
mysql_host = 'localhost'
mysql_db = 'loan'


cnopts = pysftp.CnOpts()
cnopts.hostkeys = None


engine = create_engine(f"mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}")


with pysftp.Connection(host=hostname, username=username, password=password, cnopts=cnopts) as sftp:
    print(f"Connected to {hostname}")

    sftp.cwd(remote_path)
    files = sftp.listdir()

    csv_files = [f for f in files if f.endswith('.csv')]

    for file_name in csv_files:
        with sftp.open(f"{remote_path}/{file_name}", mode='rb') as remote_file:
            buffer = BytesIO(remote_file.read())

        try:
            df = pd.read_csv(buffer)

            print(df.head())

            df.to_sql(name='loan_details', con=engine, if_exists='append', index=False)

        except Exception as e:
            print(f"error processing {file_name}: {e}")
