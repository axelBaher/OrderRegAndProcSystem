from sqlalchemy.orm import Session
from backend.app import models, schemas, crud
from backend.db.session import Engine, Session

models.Base.metadata.create_all(bind=Engine)


def init_db() -> None:
    db = Session()
    test = schemas.TestCreate(text="text_filler_text", also_text="also_text_filler_also_text")
    crud.create_test(db=db, test=test)
    db.close()


if __name__ == '__main__':
    init_db()
