from csv import reader
from glob import glob
from pathlib import Path
from random import choice
from typing import Dict, List, Optional, Tuple


class Station(object):
    id: int
    readings: Dict[float, float]
    total_fluctuation: float = 0
    last_reading: Optional[float] = None

    def __init__(self, id: int) -> None:
        self.id = id
        self.readings = {}

    def add_reading(self, date, temperature):
        self.readings[date] = temperature
        if self.last_reading is not None:
            self.total_fluctuation += abs(temperature - self.last_reading)
        self.last_reading = temperature

    def fluctuation_in_span(self, first, last):
        flux = 0
        prev = None
        for key, value in self.readings.items():
            if key < first or key > last:
                continue
            if prev is not None:
                flux += abs(value - prev)
            prev = value
        return flux


class App(object):
    stations: Dict[int, Station] = {}
    lowest = float("+inf")
    lowest_readings: List[Tuple[int, float]] = []
    highest_fluctuation: Optional[Station] = None
    data_file_path: Path = None

    def __init__(self, filename: str = "data.csv"):
        project_root = Path(__file__).parent.parent
        self.data_file_path = next(project_root.glob(f"**/{filename}"))

    def load_data(self) -> None:
        with open(self.data_file_path, "r") as data:
            lines = reader(data)
            next(lines) # skip header row
            for line in lines:
                id: int = int(line[0])
                date: float = float(line[1])
                temperature: float = float(line[2])
                try:
                    station = self.stations[id]
                except KeyError:
                    station = self.stations[id] = Station(id)
                station.add_reading(float(date), float(temperature))
                if temperature < self.lowest:
                    self.lowest = temperature
                    self.lowest_readings = [(id, date)]
                elif temperature == self.lowest:
                    self.lowest_readings.append((id, date))
                if not self.highest_fluctuation:
                    self.highest_fluctuation = station
                elif (
                    station.total_fluctuation
                    > self.highest_fluctuation.total_fluctuation
                ):
                    self.highest_fluctuation = station

    def get_lowest(self):
        return choice(self.lowest_readings)

    def get_highest_fluctuation(self):
        return self.highest_fluctuation.id

    def get_highest_for_date_range(self, first, last):
        highest = None
        highest_id = None
        for station in self.stations.values():
            flux = station.fluctuation_in_span(first, last)
            if not highest or flux > highest:
                highest = flux
                highest_id = station.id
        return highest_id
