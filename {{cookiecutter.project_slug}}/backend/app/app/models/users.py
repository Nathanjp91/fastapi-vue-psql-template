from sqlmodel import SQLModel, Field


class UserBase(SQLModel):
    name: str
    email: str
    password: str


class User(UserBase, table=True):
    id: int = Field(default=None, primary_key=True)


class SongCreate(UserBase):
    pass
