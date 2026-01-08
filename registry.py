DATA_PRODUCTS = {
    "sales" : "http://127.0.0.1:8001/sales",
    "marketing" : "http://127.0.0.1:8002/sales"
}

def list_data_products():
    return list(DATA_PRODUCTS)

def get_product_url(name : str):
    return DATA_PRODUCTS.get(name)