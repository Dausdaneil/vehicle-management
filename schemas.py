from pydantic import BaseModel
from datetime import date


class VehicleCreate(BaseModel):
    name: str
    plate_number: str


class VehicleOut(VehicleCreate):
    id: int

    class Config:
        orm_mode = True


class FuelLogCreate(BaseModel):
    vehicle_id: int
    date: date
    liters: float
    cost: float
    odometer: float


class FuelLogOut(FuelLogCreate):
    vehicle_id: int


class FuelLog(FuelLogCreate):
    id: int
    vehicle_id: int

    class Config:
        orm_mode = True
