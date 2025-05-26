from sqlalchemy.orm import Session
from models import Vehicle, FuelLog
import schemas


def create_vehicle(db: Session, vehicle: schemas.VehicleCreate):
    db_vehicle = Vehicle(**vehicle.dict())
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle


def get_vehicles(db: Session):
    return db.query(Vehicle).all()


def create_fuel_log(db: Session, log: schemas.FuelLogCreate):
    db_log = FuelLog(**log.dict())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log


def get_fuel_logs(db: Session, vehicle_id: int):
    return db.query(FuelLog).filter(FuelLog.vehicle_id == vehicle_id).order_by(FuelLog.date).all()

