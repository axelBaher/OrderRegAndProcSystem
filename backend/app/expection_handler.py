from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from fastapi import HTTPException
from starlette import status
from backend.logs import logger


class MyHTTPException(HTTPException):
    def __init__(self, status_code: int, detail: str, **kwargs):
        if status_code == status.HTTP_204_NO_CONTENT:
            logger.warning(f"Operation status code: {status_code} - {detail}")
        elif status_code == status.HTTP_201_CREATED:
            logger.info(f"Operation status code: {status_code} - {detail}")
        else:
            logger.error(f"Operation status code: {status_code} - {detail}")
        super().__init__(detail=detail, status_code=status_code, **kwargs)


class NoContentException(MyHTTPException):
    def __init__(self, detail: str = "No content", **kwargs):
        super().__init__(status_code=status.HTTP_204_NO_CONTENT, detail=detail, **kwargs)


class CreatedException(MyHTTPException):
    def __init__(self, detail: str = "Resource created", **kwargs):
        super().__init__(status_code=status.HTTP_201_CREATED, detail=detail, **kwargs)


class NotFoundException(MyHTTPException):
    def __init__(self, detail: str = "Resource not found", **kwargs):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail, **kwargs)


def handle_exceptions(db: Session, query_func, query_args, expected_status_code: int = status.HTTP_200_OK):
    try:
        result = query_func(db=db, **query_args)
        if (result is None) or (isinstance(result, list) and not result):
            raise NoContentException()
        # if :
        #     raise NotFoundException()
        if expected_status_code == status.HTTP_201_CREATED:
            raise CreatedException()
        logger.info(f"Operation successful: {query_func.__name__} completed.")
        return result
    except SQLAlchemyError as e:
        detail = f"Database error:\n{str(e)}"
        logger.error(f"Operation failed: {query_func.__name__} not completed.")
        logger.error(detail)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail)
    except HTTPException as e:
        if e.status_code in range(200, 299):
            logger.info(f"Operation successful: {query_func.__name__} completed.")
        else:
            logger.error(f"Operation failed: {query_func.__name__} not completed.")
        raise e
    except Exception as e:
        detail = f"Unhandled exception:{str(e)}"
        logger.error(detail)
        logger.error(f"Operation failed: {query_func.__name__} not completed.")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)
