from pydantic import BaseModel, ConfigDict


class TestBase(BaseModel):
    """
    Base scheme for Test model.
    """
    model_config = ConfigDict(from_attributes=True)

    text: str


class TestCreate(TestBase):
    model_config = ConfigDict(from_attributes=True)

    also_text: str
