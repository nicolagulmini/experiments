from typing import Union
from fastapi import FastAPI, Query

import wrapper # separation of concerns

app = FastAPI()
model = wrapper.Wrap()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/{item}")
async def read_string(item: str):
    return {"you typed": item}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
# si puo fare anche 
'''
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
'''

@app.get("/test_model/")
def test_model(
    x1: float = Query(0.0, description="Value for x1"),
    x2: float = Query(0.0, description="Value for x2"),
    x3: float = Query(0.0, description="Value for x3"),
    x4: float = Query(0.0, description="Value for x4"),
):
    result = model.eval(x1, x2, x3, x4)
    return {
        "input_parameters": {"x1": x1, "x2": x2, "x3": x3, "x4": x4},
        "result": result
    }
    # try typing 127.0.0.1:8000/test_model/?x1=1.0&x2=2.0&x3=3.0&x4=4.0

    