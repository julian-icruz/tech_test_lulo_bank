import setup

app = setup._create_app()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Tech Test Lulo Bank 🏦!"}