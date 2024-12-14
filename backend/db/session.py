# import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.core.config import MYSQL_CONNECTION_STRING

# from backend.core.config import ROOT_PATH

Engine = create_engine(MYSQL_CONNECTION_STRING, echo=False,
                       pool_size=20,  # Максимальное количество соединений
                       max_overflow=10,
                       pool_timeout=30,
                       pool_recycle=1800)
Session = sessionmaker(bind=Engine, autocommit=False, autoflush=False)

# if not os.path.exists(ROOT_PATH.joinpath("sqlite")):
#     os.makedirs(ROOT_PATH.joinpath("sqlite"))
