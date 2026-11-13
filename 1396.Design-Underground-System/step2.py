class UndergroundSystem:

    def __init__(self):
        self.checkedin: dict[int, tuple[str, int]] = {}
        self.total_times: dict[tuple[str, str], tuple[int, int]] = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.checkedin:
            raise ValueError(f"Customer {id} is already checked in.")
        self.checkedin[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id not in self.checkedin:
            raise ValueError(f"Customer {id} has not checked in.")

        start_station, start_time = self.checkedin.pop(id)
        duration = t - start_time
        if duration < 0:
            raise ValueError(f"Invalid travel duration ({duration}): check-out time cannot be earlier than check-in time.")

        total_time, count = self.total_times.get((start_station, stationName), (0, 0))
        self.total_times[(start_station, stationName)] = (total_time + duration, count + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if (startStation, endStation) not in self.total_times:
            raise ValueError(f"No completed trips recorded between {startStation} and {endStation}.")

        total_time, count = self.total_times[(startStation, endStation)]
        return total_time / count
