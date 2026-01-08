from fastapi  import FastAPI

app = FastAPI(title="Sales Domain")

marketing_data = [
    {'firstname': 'John', 'lastname': 'Doe'},
    {'firstname': 'Alice', 'lastname': 'Smith'},
    {'firstname': 'Michael', 'lastname': 'Johnson'},
    {'firstname': 'Emma', 'lastname': 'Williams'},
    {'firstname': 'David', 'lastname': 'Brown'},
    {'firstname': 'Sophia', 'lastname': 'Jones'},
    {'firstname': 'Daniel', 'lastname': 'Miller'},
    {'firstname': 'Olivia', 'lastname': 'Davis'},
    {'firstname': 'James', 'lastname': 'Garcia'},
    {'firstname': 'Isabella', 'lastname': 'Martinez'}
]


@app.get('/sales')
def get_sales_data():
    return {
        "data" : marketing_data,
        "owner" : "Sales Teams"
}