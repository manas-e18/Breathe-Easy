from fastapi import FastAPI
from pydantic import BaseModel
from gemini import get_route_plan

app = FastAPI()

class RouteRequest(BaseModel):
    location: str
    distance: float

@app.post("/route")
def generate_route(req: RouteRequest):
    result = get_route_plan(req.location, req.distance)
    return {
        "route": result
    }
        