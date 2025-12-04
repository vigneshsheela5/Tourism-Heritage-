# Tourism-Heritage-
For The Internship Done  At JBIET >>> ALL About Telangana Tourism &amp; Heritage


🏞️ Tourism & Heritage Backend API
FastAPI + JSON Server | Telangana Districts & Tourist Places
📌 Overview

This project is a Backend API system designed for managing Tourism & Heritage data of Telangana, built during an internship at JBIET.
The backend provides REST APIs for:

🏛️ Districts of Telangana

📍 Heritage & Tourist Places

It uses:

FastAPI for developing the API

JSON Server (db.json) as a mock database

Python service layer for interacting with JSON Server

Swagger & Thunder Client for testing

🚀 Tech Stack
Component	Technology
Backend Framework	FastAPI (Python)
Mock Database	JSON Server
HTTP Client	Python Requests
API Documentation	Swagger UI
Testing Tools	Thunder Client / Browser
Runtime	Uvicorn
📁 Project Folder Structure
internship_project/
│
├── baba/
│   ├── services/
│   │   ├── districts_service.py
│   │   ├── places_service.py
│   │   ├── districts_api.py
│   │   ├── places_api.py
│
├── db.json
├── main.py        # (optional combined API)
├── README.md
└── .venv/

⚙️ Setup Instructions
1️⃣ Install dependencies
pip install fastapi uvicorn requests json-server

2️⃣ Start JSON Server (Mock DB)

Navigate to your project folder (very important):

cd "E:\internship project"


Then run JSON Server:

json-server --watch "baba\db.json" --port 3000


This starts your mock database at:

👉 http://localhost:3000

3️⃣ Start FastAPI Backend

Move to your services folder:

cd "E:\internship project\baba\services"


Run Districts API:

uvicorn districts_api:app --reload --port 8000


Run Places API:

uvicorn places_api:app --reload --port 8000


Or run both together if you use main.py:

uvicorn main:app --reload --port 8000


Swagger Docs:

👉 http://localhost:8000/docs

📚 API Endpoints
🏛️ Districts API Endpoints
Method	Endpoint	Description
GET	/districts	Fetch all districts
GET	/districts?id=1	Fetch district by ID
GET	/districts?name=Nalgonda	Fetch by district name
POST	/districts	Add a new district
PUT	/districts/{id}	Update district information
DELETE	/districts/{id}	Delete a district
📍 Places API Endpoints
Method	Endpoint	Description
GET	/places	Fetch all places
GET	/places?id=1	Fetch place by ID
GET	/places?districts=Warangal	Fetch places by district name
POST	/places	Add a new place
PUT	/places/{id}	Update place
DELETE	/places/{id}	Delete place
🧪 API Testing Tools
✔️ Swagger UI

Automatically generated:

👉 http://localhost:8000/docs

✔️ Thunder Client / Postman

Use for testing all CRUD operations easily.

🧩 Features Implemented

✔️ Full backend API using FastAPI

✔️ JSON Server as a mock database

✔️ Service layer architecture

✔️ CRUD functionality for Districts & Places

✔️ Error handling (ID already exists, not found, etc.)

✔️ Clean folder structure

✔️ Easy to run & test

🎯 Future Enhancements

Replace JSON Server with SQLite / PostgreSQL

Add Search / Filters for places

Add authentication using JWT

Deploy API to Render / Railway

Add admin panel for data entry

📝 Conclusion

This backend project demonstrates practical experience with:

REST API development

Python FastAPI framework

API testing

Service-driven architecture

Working with mock JSON databases

It forms a solid foundation for a Tourism Information System.

If you want, I can also generate:

📌 Full 30–40 page Internship Report (PDF)
📌 PowerPoint Presentation
📌 UML / Flow Diagram
📌 Sample Test Cases

Just ask!
