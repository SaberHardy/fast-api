from database import Base, engine, SessionLocal
from fastapi import FastAPI, Body, Depends
from sqlalchemy.orm import Session
import structure_model
import models

Base.metadata.create_all(engine)
app = FastAPI()

fakeDatabase = {
    1: {'task': 'Clean car'},
    2: {'task': 'Streaming'},
    3: {'task': 'Make a test'},
}


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@app.get('/')
def get_items(session: Session = Depends(get_session)):
    items = session.query(models.Item).all()
    return items


# Get items by id
@app.get('/{id}')
def get_item(id: int, session: Session = Depends(get_session)):
    item = session.query(models.Item).get(id)
    return item


# Option 1 using the item class in structure_model model
@app.post('/')
def add_item(item: structure_model.Item, session: Session = Depends(get_session)):
    # new_id = len(fakeDatabase.keys()) + 1 # the id will auto generated
    # fakeDatabase[new_id] = {'task': item.task}
    item = models.Item(task=item.task)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


# Option 2 using body class (this is the best way to create your data)
# @app.post('/')
# def add_item(body=Body()):
#     new_id = len(fakeDatabase.keys()) + 1
#     fakeDatabase[new_id] = {'task': body['task']}
#
#     return fakeDatabase


# Option 3 manually create the request
# @app.post('/')
# def add_item(body=Body()):
#     new_id = len(fakeDatabase.keys()) + 1
#     fakeDatabase[new_id] = {'task': body['task']}
#
#     return fakeDatabase

@app.put('/{id}')
def update_item(id: int, item: structure_model.Item, session: Session = Depends(get_session)):
    item_object = session.query(models.Item).get(id)
    item_object.task = item.task
    session.commit()
    return item_object


@app.delete('/{id}')
def delete_item(id: int, session: Session = Depends(get_session)):
    item_object = session.query(models.Item).get(id)
    session.delete(item_object)
    session.commit()
    session.close()
    # del fakeDatabase[id]
    return "Item was deleted..."
