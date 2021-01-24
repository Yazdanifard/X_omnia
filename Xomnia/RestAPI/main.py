from typing import Optional
import uvicorn
import pandas as pd
import json
from fastapi import FastAPI

app = FastAPI()


df2_2 = pd.read_csv('Resources/2.2_max_min_speed.csv').drop(columns={'Unnamed: 0'})
df2_3 = pd.read_csv('Resources/2.3_avg_speed.csv').drop(columns={'Unnamed: 0'})

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/df2_2/")
def read_test():
    result = df2_2.to_json(orient="records")
    parsed = json.loads(result)
    return parsed


@app.get("/df2_3/")
def read_test():
    result = df2_3.to_json(orient="records")
    parsed = json.loads(result)
    return parsed



@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

