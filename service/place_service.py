# service/place_service.py
import requests

BASE_URL = "http://localhost:3000/places"


# fetch all places
def get_all_places():
    response = requests.get(BASE_URL)
    return response.json()


# fetch all unique place names
def get_all_place_names():
    places = get_all_places()
    names = set()
    for p in places:
        names.add(p["name"])
    return list(names)


# fetch place by ID
def get_place_by_id(place_id: int):
    response = requests.get(f"{BASE_URL}/{place_id}")
    if response.status_code == 404:
        return None
    return response.json()


# fetch places by district_id
def get_places_by_district(district_id: int):
    response = requests.get(f"{BASE_URL}?district_id={district_id}")
    data = response.json()
    if not data:
        return None
    return data


# fetch places by name
def get_places_by_name(name: str):
    response = requests.get(f"{BASE_URL}?name={name}")
    data = response.json()
    if not data:
        return None
    return data


def get_place_count():
    return len(get_all_places())


def add_place(place_data: dict):
    if get_place_by_id(place_data["id"]):
        return {"error": "Place with this ID already exists."}
    response = requests.post(BASE_URL, json=place_data)
    return response.json()


def update_place(place_id: int, place_data: dict):
    if not get_place_by_id(place_id):
        return {"error": "Place not found."}
    response = requests.put(f"{BASE_URL}/{place_id}", json=place_data)
    return response.json()


def delete_place(place_id: int):
    if not get_place_by_id(place_id):
        return {"error": "Place not found."}

    response = requests.delete(f"{BASE_URL}/{place_id}")

    if response.status_code == 200 or response.status_code == 204:
        return {"message": "Place deleted successfully."}
    else:
        return {"error": "Failed to delete place."}
