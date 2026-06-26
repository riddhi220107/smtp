import os
from dotenv import load_dotenv
load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = os.getenv("SMTP_PORT")
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

db_connect_host = os.getenv("db_connect_host")
db_connect_name = os.getenv("db_connect_name")
db_connect_user = os.getenv("db_connect_user")
db_connect_password = os.getenv("db_connect_password")
db_connect_port = os.getenv("db_connect_port")