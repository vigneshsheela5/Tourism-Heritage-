# service/places_api.py
from fastapi import APIRouter, HTTPException
from . import place_service

router = APIRouter()


# ------- GET all -------
@router.get("/", summary="Get All Places")
def get_all_places():
    return place_service.get_all_places()


# ------- GET by id -------
@router.get("/{place_id}", summary="Get Place By ID")
def get_place_by_id(place_id: int):
    place = place_service.get_place_by_id(place_id)
    if not place:
        raise HTTPException(status_code=404, detail="Place not found")
    return place


# ------- GET by district -------
@router.get("/search/by-district", summary="Get Places By District")
def get_places_by_district(district_id: int):
    places = place_service.get_places_by_district(district_id)
    if not places:
        raise HTTPException(
            status_code=404,
            detail="No places found for this district_id"
        )
    return places


# ------- GET by name -------
@router.get("/search/by-name", summary="Search Places By Name")
def get_places_by_name(name: str):
    places = place_service.get_places_by_name(name)
    if not places:
        raise HTTPException(status_code=404, detail="Place not found")
    return places


# ------- POST (create) -------
@router.post("/", summary="Add New Place")
def add_new_place(place: dict):
    res = place_service.add_place(place)
    if isinstance(res, dict) and res.get("error"):
        raise HTTPException(status_code=400, detail=res["error"])
    return res


# ------- PUT (update) -------
@router.put("/{place_id}", summary="Update Place")
def update_place(place_id: int, place: dict):
    res = place_service.update_place(place_id, place)
    if isinstance(res, dict) and res.get("error"):
        raise HTTPException(status_code=404, detail=res["error"])
    return res


# ------- DELETE -------
@router.delete("/{place_id}", summary="Delete Place")
def delete_place(place_id: int):
    res = place_service.delete_place(place_id)
    if isinstance(res, dict) and res.get("error"):
        raise HTTPException(status_code=404, detail=res["error"])
    return {"message": "Place deleted successfully"}
