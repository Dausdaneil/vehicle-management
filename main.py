from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal, engine
from pydantic import BaseModel

# Create tables
models.Base.metadata.create_all(bind=engine)

router = APIRouter()

app = FastAPI()


class StatusUpdate(BaseModel):
    new_status: str


# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Root
@app.get("/")
def read_root():
    return {"message": "API is working!"}


# POST /vehicles
@app.post("/vehicles/", response_model=schemas.VehicleOut)
def create_vehicle(vehicle: schemas.VehicleCreate, db: Session = Depends(get_db)):
    db_vehicle = models.Vehicle(**vehicle.dict())
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle

# POST /vehicles/{vehicle_id}/status
@router.put("/vehicles/{vehicle_id}/status")
def update_vehicle_status(vehicle_id: int, data: StatusUpdate, db: Session = Depends(get_db)):
    vehicle = db.query(models.Vehicle).filter(models.Vehicle.id == vehicle_id).first()
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")

    vehicle.status = data.new_status
    db.commit()
    db.refresh(vehicle)
    return {"message": "Status updated", "vehicle": vehicle}


# GET /vehicles
@app.get("/vehicles/", response_model=list[schemas.VehicleOut])
def read_vehicles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Vehicle).order_by(models.Vehicle.id).offset(skip).limit(limit).all()

# POST /fuel_logs
@app.post("/fuel_logs/", response_model=schemas.FuelLogOut)
def create_fuel_log(fuel_log: schemas.FuelLogCreate, db: Session = Depends(get_db)):
    # Optional: check if vehicle exists
    vehicle = db.query(models.Vehicle).filter(models.Vehicle.id == fuel_log.vehicle_id).first()
    if vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")

    db_fuel_log = models.FuelLog(**fuel_log.dict())
    db.add(db_fuel_log)
    db.commit()
    db.refresh(db_fuel_log)
    return db_fuel_log


# Get /fuel_logs
@app.get("/fuel_logs/", response_model=list[schemas.FuelLog])
def read_fuel_logs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.FuelLog).offset(skip).limit(limit).all()


app.include_router(router)