# service/districts_api.py
from fastapi import APIRouter, HTTPException
from . import district_service

router = APIRouter()


# ------- GET all -------
@router.get("/", summary="Get All Districts")
def get_all_districts():
    return district_service.get_all_districts()


# ------- GET by id -------
@router.get("/{district_id}", summary="Get District By ID")
def get_district_by_id(district_id: int):
    district = district_service.get_district_by_id(district_id)
    if not district:
        raise HTTPException(status_code=404, detail="District not found")
    return district


# ------- GET by name (search) -------
@router.get("/search/by-name", summary="Search District By Name")
def get_district_by_name(name: str):
    districts = district_service.get_district_by_name(name)
    if not districts:
        raise HTTPException(status_code=404, detail="District not found")
    return districts


# ------- POST (create) -------
@router.post("/", summary="Add New District")
def add_new_district(district: dict):
    res = district_service.add_district(district)
    if isinstance(res, dict) and res.get("error"):
        raise HTTPException(status_code=400, detail=res["error"])
    return res


# ------- PUT (update) -------
@router.put("/{district_id}", summary="Update District")
def update_district(district_id: int, district: dict):
    res = district_service.update_district(district_id, district)
    if isinstance(res, dict) and res.get("error"):
        raise HTTPException(status_code=404, detail=res["error"])
    return res


# ------- DELETE -------
@router.delete("/{district_id}", summary="Delete District")
def delete_district(district_id: int):
    res = district_service.delete_district(district_id)
    if isinstance(res, dict) and res.get("error"):
        raise HTTPException(status_code=404, detail=res["error"])
    return {"message": "District deleted successfully"}

