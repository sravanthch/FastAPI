from fastapi import FastAPI
from models import Product  

app = FastAPI()

Products = [
        Product(1,"Iphone","Base Model",700,6),
        Product(2,"Samsung","Galaxy",800,4)
    ]

@app.get("/")
def greet():
    return "Hello World"


@app.get("/products")
def get_all_products():
    return Products