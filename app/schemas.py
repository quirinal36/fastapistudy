from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    phone: str

class User(UserCreate):
    id: int

    class Config:
        from_attribute = True
