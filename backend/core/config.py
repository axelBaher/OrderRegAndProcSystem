import os
from pathlib import Path
from sqlalchemy import URL

ROOT_PATH = Path(__file__).resolve().parent.parent.parent
DATABASE_PATH = ROOT_PATH / "sqlite" / "axelbaher.db"
SQLITE_DB_URL = URL.create(drivername="sqlite", database=f"{DATABASE_PATH}")
SSL_KEY_PATH = ROOT_PATH / "SSL" / "key.pem"
SSL_CERT_PATH = ROOT_PATH / "SSL" / "cert.pem"
SSL_KEY_PASSWORD_PATH = ROOT_PATH / "SSL" / "key_password"
MYSQL_DBCONFIG = {"engine": "mysql",
                  "host": "localhost",
                  "user": "axelBaher",
                  "password": "axelBaher",
                  "port": 3306,
                  "database": "main"}
MYSQL_CONNECTION_STRING = "{engine}://{user}:{password}@{host}:{port}/{database}?charset=utf8".format(**MYSQL_DBCONFIG)
LOG_CONSOLE_ENABLED = True
LOG_FILE_ENABLED = True
LOG_PATH = ROOT_PATH / "backend" / "logs"
