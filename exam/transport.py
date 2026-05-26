from abc import ABC, abstractmethod
from typing import List, Dict, Optional

class Transport(ABC):
    def __init__(self, route_number: str, departure: str):
        self.route_number = route_number
        self.departure = departure

    @abstractmethod
    def get_schedule(self) -> dict:
        pass

class Bus(Transport):
    def __init__(self, route_number: str, departure: str, stops: List[str]):
        super().__init__(route_number, departure)
        self.stops = stops

    def get_schedule(self) -> dict:
        return {
            "type": "bus",
            "route_number": self.route_number,
            "departure": self.departure,
            "stops": self.stops
        }

class Train(Transport):
    def __init__(self, route_number: str, departure: str, stations: List[str], travel_time_min: int):
        super().__init__(route_number, departure)
        self.stations = stations
        self.travel_time_min = travel_time_min

    def get_schedule(self) -> dict:
        return {
            "type": "train",
            "route_number": self.route_number,
            "departure": self.departure,
            "stations": self.stations,
            "travel_time_min": self.travel_time_min
        }

class Schedule:
    def __init__(self):
        self.__routes: Dict[str, Transport] = {}

    def add_route(self, transport: Transport):
        self.__routes[transport.route_number] = transport

    def find_route(self, route_number: str) -> Optional[Transport]:
        return self.__routes.get(route_number)

    def list_routes(self) -> List[dict]:
        return [t.get_schedule() for t in self.__routes.values()]
