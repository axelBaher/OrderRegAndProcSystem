from pydantic import BaseModel


class TestBase(BaseModel):
    """
    Base scheme for Test model.
    """
    text: str

    class Config:
        from_attributes = True


class TestCreate(TestBase):
    also_text: str

    class Config:
        from_attributes = True
