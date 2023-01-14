from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from sqlmodel import Session, select
from typing import List
from models import engine
from models import Movie

app = FastAPI()

@app.get("/")
def index():
    return RedirectResponse("/docs")

@app.get("/movies/", response_model=List[Movie])
def list_movies():
    with Session(engine) as session:
        return session.query(Movie).all()

@app.get("/movies/{pk}/", response_model=Movie)
def detail_movie():
    with Session(engine) as session:
        return session.query(Movie).first()

@app.put("/movies/{pk}/")
def update_movie(pk: int, movie: Movie):
    with Session(engine) as session:
        instance = session.query(Movie).filter(Movie.id==pk).first()
        for k, v in movie.dict().items():
            if v:
                setattr(instance, k, v)
        session.commit()
        return {"message": "Updates successfully!"}

@app.post("/movies/")
def create_movies(movie: Movie):
    with Session(engine) as session:
        session.add(movie)
        session.commit()
        return {"message": f"Movie {movie.id} created "}