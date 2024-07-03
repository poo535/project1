from fastapi import FastAPI,Body
from typing import Dict
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/greet/{name}") 
def greet(name: str): 
    return f"Hello {name}"

# This example is from deepak

@app.post("/greetpost/")
def greet(request=Body(...)):
    name = request.get("name")
    return {"message": f"Hello {name}"}

@app.get("/items/")
def read_items(category: str, brand: str): 
    return f"Category is : {category} and brand is {brand}"

# POST REQUEST CALLS VERY IMPORTANT

from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str
    price: float

@app.post("/items/")
def create_item(item: Item):
    return item

class car(BaseModel):

    make: str
    model: str
    year: float

@app.post("/car/")
def create_car(mmy: car):
    return car


@app.get("/itemsget/")
def read_items():
    items = [Item(name="Foo", description="A new item", price=45.2), 
             Item(name="Bar", description="Another item", price=10.5)]
    return items

class Issue(BaseModel):
    e2e_id: str
    description: str

# @app.post("/tester_assisyant/")
# def get_resolution(issue:Issue):

    


