from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

class Memo(BaseModel):
    id:int
    content:str
    
memos =[]

app = FastAPI()

@app.post("/memos")
def create_memo(memo:Memo):
    memos.append(memo)
    return "추가완료"


@app.get("/memos")
def read_memo():
    return memos

app.mount("/",StaticFiles(directory='static',html=True),name= 'static')