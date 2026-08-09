class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        days_to_wait = [0] * len(temperatures)
        unresolved_day_indices = []
        for today_index, temperature in enumerate(temperatures):
            while (
                unresolved_day_indices
                and temperatures[unresolved_day_indices[-1]] < temperature
            ):
                unresolved_day_index = unresolved_day_indices.pop()
                days_to_wait[unresolved_day_index] = today_index - unresolved_day_index
            unresolved_day_indices.append(today_index)

        return days_to_wait
