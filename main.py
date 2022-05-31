from fastapi import FastAPI

app = FastAPI()

fakeDatabase = {
    1: {'task': 'Clean car'},
    2: {'task': 'Streaming'},
    3: {'task': 'Make a test'},
}

@app.get('/')
def get_items():
    return fakeDatabase
