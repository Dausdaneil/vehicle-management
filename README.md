# 🚗 Vehicle Management App

This is a simple FastAPI application for managing company vehicles and their fuel logs. It allows users to:

- Add new vehicles
- View a list of registered vehicles
- Add fuel log entries (liters, cost, odometer, date)
- View all fuel logs

## 📦 Tech Stack

- **Backend Framework**: FastAPI
- **Database**: PostgreSQL (via SQLAlchemy ORM)
- **Validation**: Pydantic
- **Language**: Python

## 📂 Features

### Vehicles
- `POST /vehicles/` — Add a new vehicle
- `GET /vehicles/` — List all vehicles

### Fuel Logs
- `POST /fuel_logs/` — Add a new fuel log entry
- `GET /fuel_logs/` — List all fuel logs

## 🛠️ Setup

1. **Clone the repo**

   git clone https://github.com/Dausdaneil/vehicle-management.git
   cd vehicle-management
   
2. **Install dependencies**
   
   pip install -r requirements.txt

3. **Run the app**
   
   uvicorn main:app --reload

4. **Access the API docs**

   Visits: http//127.0.0.1:8000/docs
   
Created by @Dausdaneil

Note: I will be developing more features for this app from time to time. Let me know if you want to add a short section for PostgreSQL setup or database info.