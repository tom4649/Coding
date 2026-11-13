class UndergroundSystem:

    def __init__(self):
        self.checkedin: dict[int, tuple[str, int]] = {}
        self.total_times: dict[tuple[str, str], tuple[int, int]] = {}


    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.checkedin:
            raise ValueError("duplicated id")
        self.checkedin[id] = (stationName, t)


    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id not in self.checkedin:
            raise ValueError("check-out before check-in")
        start_station, start_time = self.checkedin.pop(id)
        if t - start_time < 0:
            raise ValueError("invalid time interval")
        total_time, count = self.total_times.get((start_station, stationName), (0, 0))
        self.total_times[(start_station, stationName)] = (total_time + (t - start_time), count + 1)


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if (startStation, endStation) not in self.total_times:
            raise ValueError("no record of the station pair")
        return self.total_times[(startStation, endStation)][0] / self.total_times[(startStation, endStation)][1]



# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
