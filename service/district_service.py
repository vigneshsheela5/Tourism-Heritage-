# service/district_service.py
import requests

BASE_URL = "http://localhost:3000/districts"


# fetch all districts
def get_all_districts():
    response = requests.get(BASE_URL)
    return response.json()


# fetch all unique district names
def get_all_district_names():
    districts = get_all_districts()
    names = set()
    for d in districts:
        names.add(d["name"])
    return list(names)


# fetch district by ID
def get_district_by_id(district_id: int):
    # json-server style: /districts/5
    response = requests.get(f"{BASE_URL}/{district_id}")
    if response.status_code == 404:
        return None
    return response.json()


# fetch districts by name (can be multiple matches)
def get_district_by_name(name: str):
    # json-server style: /districts?name=Hyderabad
    response = requests.get(f"{BASE_URL}?name={name}")
    data = response.json()
    if not data:
        return None
    return data


# count
def get_district_count():
    return len(get_all_districts())


# add a district
def add_district(district_data: dict):
    # check whether district already exists with same id
    if get_district_by_id(district_data["id"]):
        return {"error": "District with this ID already exists."}

    response = requests.post(BASE_URL, json=district_data)
    return response.json()


# update a district
def update_district(district_id: int, district_data: dict):
    if not get_district_by_id(district_id):
        return {"error": "District not found."}

    response = requests.put(f"{BASE_URL}/{district_id}", json=district_data)
    return response.json()


# delete a district
def delete_district(district_id: int):
    if not get_district_by_id(district_id):
        return {"error": "District not found."}

    response = requests.delete(f"{BASE_URL}/{district_id}")

    if response.status_code == 200 or response.status_code == 204:
        return {"message": "District deleted successfully."}
    else:
        return {"error": "Failed to delete district."}

