from fastapi import FastAPI, Body
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


# Option 1 using the item class in structure_model model
# @app.post('/')
# def add_item(item: structure_model.Item):
#     new_id = len(fakeDatabase.keys()) + 1
#     fakeDatabase[new_id] = {'task': item.task}
#
#     return fakeDatabase


# Option 2 using body class (this is the best way to create your data)
@app.post('/')
def add_item(body=Body()):
    new_id = len(fakeDatabase.keys()) + 1
    fakeDatabase[new_id] = {'task': body['task']}

    return fakeDatabase


# Option 3 manually create the request
# @app.post('/')
# def add_item(body=Body()):
#     new_id = len(fakeDatabase.keys()) + 1
#     fakeDatabase[new_id] = {'task': body['task']}
#
#     return fakeDatabase

@app.put('/{id}')
def update_item(id: int, item: structure_model.Item):
    fakeDatabase[id]['task'] = item.task
    return fakeDatabase


@app.delete('/{id}')
def delete_item(id: int):
    del fakeDatabase[id]
    return fakeDatabase
