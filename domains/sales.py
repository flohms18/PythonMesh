from fastapi  import FastAPI

app = FastAPI(title="Sales Domain")

sales_data = [
    {'customer_id' : 1, 'item_purchased' : 'television','Loyalty_Card' : True},
    {'customer_id' : 2, 'item_purchased' : 'computer','Loyalty_Card' : False},
    {'customer_id' : 3, 'item_purchased' : 'smartphone','Loyalty_Card' : True},
    {'customer_id' : 4, 'item_purchased' : 'book','Loyalty_Card' : False},
    {'customer_id' : 5, 'item_purchased' : 'pen','Loyalty_Card' : True},

]

@app.get('/sales')
def get_sales_data():
    return {
        "data" : sales_data,
        "owner" : "Sales Team"
    }