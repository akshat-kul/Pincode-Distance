from fastapi import FastAPI
import uvicorn
from pincode.routers import pincode_distance_router

app = FastAPI(
    title="Pincode Distance API",
)

app.include_router(pincode_distance_router, prefix="/pincode")

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)

