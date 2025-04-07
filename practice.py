from fastapi import FastAPI,Path
from enum import Enum

app=FastAPI()

class Avalilable_laptopes(str,Enum):
    Laptops_name='Laptops_name'
    price='price'

student={
    'name':['kunal','rohan','jatin'],
    'roll_no':['1','2','4'],
    'age':['21','23','24']
}

laptops_deal={
    'Laptops_name':['Acer','lenovo','HP'],
    'price':['50,000','40,000','30,000']
}

coupon_code={
    1:"20%",
    2:"30%",
    3:"40%"
}

@app.get('/home')
def home_page():
    return 'this is our home page'

@app.get('/student_details/{student_info}')
def student_details(student_info=Path (...,description='Enter your student detail here')):
    return{'this is our student detail':student.get(student_info)}


@app.get('/best_laptops/{laptops}')
def best_laptops(laptops:Avalilable_laptopes):
    return{'this is our best laptop':laptops_deal.get(laptops)}

@app.get('/get_coupen/{code}')
def get_coupen(code:int=Path(...,description="Enter your coupen code")):
    return{'this is our coupon code':coupon_code.get(code)}

