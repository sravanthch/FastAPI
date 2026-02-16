from fastapi import FastAPI
from models import Product  

app = FastAPI()

Products = [
        Product(id=1,name="Iphone",description="Base Model",price=700,quantity=6),
        Product(id=2,name="Samsung",description="Galaxy",price=800,quantity=4)
    ]

@app.get("/")
def greet():
    return "Hello World"


@app.get("/products")
def get_all_products():
    return Products