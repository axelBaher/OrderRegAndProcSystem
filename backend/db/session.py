# import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.core.config import MYSQL_CONNECTION_STRING
# from backend.core.config import ROOT_PATH

Engine = create_engine(MYSQL_CONNECTION_STRING, echo=False)
Session = sessionmaker(bind=Engine, autocommit=False, autoflush=False)

# if not os.path.exists(ROOT_PATH.joinpath("sqlite")):
#     os.makedirs(ROOT_PATH.joinpath("sqlite"))
