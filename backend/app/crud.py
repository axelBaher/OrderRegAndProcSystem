from sqlalchemy.orm import Session, Query
from backend.app import models as m, schemas as shm


def create_test(db: Session, test: shm.TestCreate) -> m.Test:
    test_dict = test.dict()
    db_test = m.Test(**test_dict)
    db.add(db_test)
    db.commit()
    db.refresh(db_test)
    return db_test


# noinspection PyTypeChecker
def get_test(db: Session, test_id: int) -> Query:
    query = db.query(m.Test).filter(m.Test.id == test_id)
    return query
