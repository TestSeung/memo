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

@app.put("/memos/{memo_id}")
def put_memo(req_memo:Memo):
    for memo in memos:
        if memo.id==req_memo.id:
            memo.content = req_memo.content
            return '성공했습니다.'
    return '그런 메모는 없습니다.'

@app.delete("/memos/{memo_id}")
def delete_memo(memo_id:int): #매개변수 유형 지정
    for index,memo in enumerate(memos): #배열의 index값을 같이 뽑아줌
        if memo.id==memo_id:
            memos.pop(index)
            return '성공했습니다.'
    return '그런 메모는 없습니다.'

app.mount("/",StaticFiles(directory='static',html=True),name= 'static')