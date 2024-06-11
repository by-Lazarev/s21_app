# models.py

from pydantic import BaseModel, Field, ValidationError, model_validator
from typing import List
from enum import Enum

class ShipClass(str, Enum):
    CORVETTE = "Corvette"
    FRIGATE = "Frigate"
    CRUISER = "Cruiser"
    DESTROYER = "Destroyer"
    CARRIER = "Carrier"
    DREADNOUGHT = "Dreadnought"

class Officer(BaseModel):
    first_name: str
    last_name: str
    rank: str

class Spaceship(BaseModel):
    alignment: str
    name: str
    ship_class: ShipClass
    length: float
    crew_size: int
    armed: bool
    officers: List[Officer]

    @model_validator(mode='after')
    def validate_spaceship(cls, values):
        ship_class = values.ship_class
        length = values.length
        crew_size = values.crew_size
        armed = values.armed
        alignment = values.alignment
        name = values.name

        class_length_limits = {
            ShipClass.CORVETTE: (80, 250),
            ShipClass.FRIGATE: (300, 600),
            ShipClass.CRUISER: (500, 1000),
            ShipClass.DESTROYER: (800, 2000),
            ShipClass.CARRIER: (1000, 4000),
            ShipClass.DREADNOUGHT: (5000, 20000),
        }

        class_crew_limits = {
            ShipClass.CORVETTE: (4, 10),
            ShipClass.FRIGATE: (10, 15),
            ShipClass.CRUISER: (15, 30),
            ShipClass.DESTROYER: (50, 80),
            ShipClass.CARRIER: (120, 250),
            ShipClass.DREADNOUGHT: (300, 500),
        }

        # Проверка длины
        if ship_class in class_length_limits:
            min_len, max_len = class_length_limits[ship_class]
            if length is None or not (min_len <= length <= max_len):
                raise ValueError(f"Length must be between {min_len} and {max_len} for class {ship_class}")

        # Проверка размера экипажа
        if ship_class in class_crew_limits:
            min_crew, max_crew = class_crew_limits[ship_class]
            if crew_size is None or not (min_crew <= crew_size <= max_crew):
                raise ValueError(f"Crew size must be between {min_crew} and {max_crew} for class {ship_class}")

        # Проверка вооружения
        if ship_class == ShipClass.CARRIER and armed:
            raise ValueError("Carriers cannot be armed.")

        # Проверка имени для враждебных кораблей
        if alignment == "Enemy" and name != "Unknown":
            raise ValueError("Enemy ships must have name 'Unknown'")

        return values

