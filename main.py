from fastapi import FastAPI


app = FastAPI()


@app.get("/test")
def read_root():
    return {"message": "The server is up and running!!!"}