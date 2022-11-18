from fastapi import FastAPI
from pydantic import BaseModel
from dal.index import createBook, getAllBooks, updateBook, deleteBook
import uvicorn

app = FastAPI()


class Book(BaseModel):
    title: str
    author: str
    cost: float


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/createBook")
def root(book: Book):
    result = createBook(book.title, book.author, book.cost)
    return {"result": result}


@app.get("/getAllBooks")
async def root():
    result = getAllBooks()
    return {"result": result}


@app.put("/editBook")
def root(id: int, title: str, author: str, cost: str):
    result = updateBook(id, title, author, cost)
    return {"result": result}


@app.delete("/")
def root(id: int):
    result = deleteBook(id)
    return {"result": result}
