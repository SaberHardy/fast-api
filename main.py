from fastapi import FastAPI
import structure_model

app = FastAPI()

fakeDatabase = {
    1: {'task': 'Clean car'},
    2: {'task': 'Streaming'},
    3: {'task': 'Make a test'},
}


@app.get('/')
def get_items():
    return fakeDatabase


# Get items by id
@app.get('/{id}')
def get_item(id: int):
    return fakeDatabase[id]


@app.post('/')
def add_item(item: structure_model.Item):
    new_id = len(fakeDatabase.keys()) + 1
    fakeDatabase[new_id] = {'item': item.task}

    return fakeDatabase
