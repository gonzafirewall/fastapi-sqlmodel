from sqlmodel import SQLModel, Field
from typing import Optional
from sqlmodel import create_engine


engine = create_engine("sqlite:///database.sqlite")


class Movie(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    overview: str 
    year: int

SQLModel.metadata.create_all(bind=engine)