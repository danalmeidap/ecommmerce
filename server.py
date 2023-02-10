from fastapi import FastAPI
from src.infra.sqlalchemy.config.database import create_db

app = FastAPI()

@app.get("/products", tags=['products'])
async def products_list():
    return {"products list": "products List"}


@app.get("/products/{product_id}", tags=['products'])
async def get_product_by_id(product_id):
    return {"msg": f"Product with id {product_id}"}


@app.post("/products", tags=['products'])
async def create_product():
    return {"msg": "product created"}


@app.put("/products/{product_id}",tags= ["products"])
async def update_product(product_id):
    return {"msg": f"product with id {product_id} was updated"}


@app.delete("/products/{product_id}",tags=["products"])
async def delete_product(product_id):
    return {"msg": f"product with id {product_id} was deleted"}
