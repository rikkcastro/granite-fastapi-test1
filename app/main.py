from fastapi import FastAPI
from app.routes import router

# Create FastAPI app
app = FastAPI()

# Include the router with the model-related routes
app.include_router(router)
