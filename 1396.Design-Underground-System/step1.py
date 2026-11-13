import collections

class UndergroundSystem:

    def __init__(self):
        self.checkedin = {} # id: (station, time)
        self.times = collections.defaultdict(list)


    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.checkedin:
            raise ValueError("duplicated id")
        self.checkedin[id] = (stationName, t)


    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id not in self.checkedin:
            raise ValueError("check-out before check-in")
        start_station, start_time = self.checkedin[id]
        if t - start_time < 0:
            raise ValueError("in valid time interval")
        self.times[(start_station, stationName)].append(t - start_time)
        self.checkedin.pop(id)


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.times[(startStation, endStation)]) / len(self.times[(startStation, endStation)])



# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
