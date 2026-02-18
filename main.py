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

@app.get("/products/{id}")
def getById(id:int):
    for product in Products:
        if product.id == id:
            return product
    return "Not Found"    


@app.post("/product")
def add_product(product: Product):
    Products.append(product)
    return product

@app.put("/product/{id}")
def update_product(id: int, product: Product):
    for i in range(len(Products)):
        if Products[i].id == id:
            Products[i] = product
            return "Product Updated Successfully"
    return "No Product Found"    

@app.delete("/product/{id}")
def delete_product(id:int):
    for i in range(len(Products)):
        if Products[i].id == id:
            del Products[i]
            return "Product Deleted Successfully"
    return "Failed To Delete Product"    


