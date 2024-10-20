import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.core.config import SQLITE_DB_URL, ROOT_PATH

Engine = create_engine(SQLITE_DB_URL, echo=False)
Session = sessionmaker(bind=Engine, autocommit=False, autoflush=False)

if not os.path.exists(ROOT_PATH.joinpath("sqlite")):
    os.makedirs(ROOT_PATH.joinpath("sqlite"))
