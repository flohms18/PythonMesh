from fastapi import FastAPI,HTTPException
import httpx
from registry import list_data_products, get_product_url

app = FastAPI(title="Python_Mesh")

@app.get("/products")
def products():
    return {
        "products" : list_data_products
    }

@app.get("products/{product_name}")
def fetch_product(product_name: str):
    url = get_product_url(product_name)
    if not url:
        raise HTTPException(status_code=404,detail="Data Product not found")
    try: 
        response = httpx.get(url,timeout=5)
        response.raise_for_status()
        return response.json()
    except httpx.HTTPError as e: 
        raise HTTPException(status_code=500,detail=str(e))
