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

## 🛠️ Setup Instructions

1. **Clone the repo**

   ```bash
   git clone https://github.com/Dausdaneil/vehicle-management.git
   cd vehicle-management
