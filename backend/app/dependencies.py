from fastapi.security import HTTPBearer

from ..db.session import Session

security = HTTPBearer()


def get_db():
    """
    Provides db session for each request, automatically closing after request completion.
    """
    db = Session()
    try:
        yield db
    finally:
        db.close()
