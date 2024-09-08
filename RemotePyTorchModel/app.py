from typing import Union, Annotated
from fastapi import FastAPI, Query, File, UploadFile

classes = [
    "T-shirt/top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle boot",
]

import wrapper # separation of concerns
import cache

app = FastAPI()
model = wrapper.Wrap()
LRUcache = cache.Cache(3)

@app.post("/upload")
def upload(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()
    hashedImage = hash(contents)
    class_ = LRUcache.get(hashedImage)
    if class_ == -1: 
        class_ = model.eval(contents)
        LRUcache.insert(hashedImage, class_)
    print([(el.key, el.value) for el in LRUcache.cache])
    return {'Predicted class:': classes[class_]}