from typing import Union, Annotated
from fastapi import FastAPI, Query, File, UploadFile


import wrapper # separation of concerns

app = FastAPI()
model = wrapper.Wrap()

@app.post("/upload")
def upload(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        with open(file.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()
    return model.eval(contents)