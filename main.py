from fastapi import FastAPI, Path, Query, HTTPException, status,UploadFile,File
from typing import Optional
from pydantic import BaseModel
from PIL import Image
import io
from fastapi.responses import StreamingResponse

app = FastAPI()

class Item(BaseModel):
    name: str
    price: int
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[int] = None  # changed to int (was str)
    brand: Optional[str] = None

inventory = {}

# Path Parameter
@app.get('/get-item/{item_id}')
def get_item(item_id: int = Path(..., description='The ID of the item you want to view')):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item not found")
    return inventory[item_id]

# Query Parameter
@app.get('/get-by-name')
def get_item_by_name(name: Optional[str] = None, test: int = Query(...)):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    raise HTTPException(status_code=404, detail="Item name not found")

# Request Body
@app.post('/create-item/{item_id}')
def create_item(item_id: int, item: Item):  # Use Item, not UpdateItem
    if item_id in inventory:
        return {'error': 'ID already exists'}
    inventory[item_id] = item
    return inventory[item_id]

# Update
@app.put('/update-item/{item_id}')
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        return {'error': 'Item ID does not exist'}

    if item.name is not None:
        inventory[item_id].name = item.name

    if item.price is not None:
        inventory[item_id].price = item.price

    if item.brand is not None:
        inventory[item_id].brand = item.brand

    return inventory[item_id]

# Delete
@app.delete('/delete-item')
def delete_item(item_id: int = Query(..., description='The ID of the item you want to delete')):
    if item_id not in inventory:
        return {'error': 'ID does not exist'}
    del inventory[item_id]
    return {'success': "Item deleted"}


#convert image to black and white
@app.post('/convert-image/')
def convert_image_to_black_white(file:UploadFile=File(...)):
    try:
        image=Image.open(file.file).convert('L')#grayscale
        buf=io.BytesIO()
        image.save(buf,format='PNG')
        buf.seek(0)
        return StreamingResponse(buf,media_type='image/png')
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Image processing failed: {str(e)}")




