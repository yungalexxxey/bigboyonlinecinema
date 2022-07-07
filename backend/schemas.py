from pydantic import BaseModel


class Film(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        orm_mode = True


class DisplayFilms(BaseModel):
    films: list[Film] = []

    class Config:
        orm_mode = True
