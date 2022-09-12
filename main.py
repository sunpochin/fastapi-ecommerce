# main.py

from fastapi import FastAPI
import json

f = open('newspaper.json')
data = json.load(f)
for i in data:
    print(i)
f.close()

# newspapers = {
#   'name': 'cityam',
#   'address': 'https://www.cityam.com/london-must-become-a-world-leader-on-climate-change-action/',
#   'base': ''
#   }

app = FastAPI()

@app.get("/")
async def root():
  return {"news": data}
    # return {"message": "Hello World"}

@app.post("/carts/")
async def root():
  return {"news": data}
