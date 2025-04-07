from fastapi import FastAPI
from enum import Enum

app=FastAPI()

class AvailableCuisine(str,Enum):
    indian="indian"
    american="american"
    italian="italian"

food_items= {
    'indian':['samosa','dal chawal', 'paneer'],
    'italian':['pizza','ravillo'],
    'american':['hot-dog','burger']
}

coupen_code={
    1:'10%',
    2:'20%',
    3:'30%'
}

@app.get('/hello/{name}')
async def hello(name):
    return f"hello how are you {name}"

@app.get('/get_items/{cuisine}')
async def get_items(cuisine:AvailableCuisine):
    return food_items.get(cuisine)

@app.get('/coupens_code/{code}')
async def coupens_code(code:int):
    return {'discount_amount':coupen_code.get(code)}