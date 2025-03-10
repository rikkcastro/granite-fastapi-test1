from fastapi import APIRouter
from pydantic import BaseModel
from app.model import generate_text

# Create a FastAPI router
router = APIRouter()

# Define the request data model
class RequestData(BaseModel):
    input_text: str

# Define the /generate route
@router.post("/generate")
async def generate(request: RequestData):
    """Generate text from the provided input"""
    input_text = request.input_text
    generated_text = generate_text(input_text)
    return {"generated_text": generated_text}
