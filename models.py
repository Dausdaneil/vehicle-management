from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    plate_number = Column(String, unique=True, index=True)
    status = Column(String, default="Active")

    fuel_logs = relationship("FuelLog", back_populates="vehicle")


class FuelLog(Base):
    __tablename__ = "fuel_logs"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    date = Column(Date)
    liters = Column(Float)
    cost = Column(Float)
    odometer = Column(Float)

    vehicle = relationship("Vehicle", back_populates="fuel_logs")
