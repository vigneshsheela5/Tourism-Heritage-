from fastapi import FastAPI
from service.districts_api import router as districts_router
from service.places_api import router as places_router

app = FastAPI(title="Telangana")

# group routes under /districts and /places
app.include_router(districts_router, prefix="/districts", tags=["Districts"])
app.include_router(places_router, prefix="/places", tags=["Places"])
