import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter_t = collections.Counter(t)
        counter_window = collections.Counter(s)
        for key, count in counter_t.items():
            if counter_window.get(key, 0) < count:
                return ""

        first = 0
        while s[first] not in counter_t:
            first += 1

        last = len(s) - 1
        while first < last:
            while s[last] not in counter_t:
                last -= 1
            if counter_t[s[last]] >= counter_window[s[last]]:
                break
            counter_window[s[last]] -= 1
            last -= 1

        min_window_first = first
        min_window_last = last
        min_window_size = last - first + 1
        while first < len(s) - 1:
            if counter_window[s[first]] <= counter_t[s[first]]:
                next_last = last + 1
                while next_last < len(s) and s[next_last] != s[first]:
                    counter_window[s[next_last]] += 1
                    next_last += 1
                if next_last == len(s):
                    break
                last = next_last
            else:
                counter_window[s[first]] -= 1

            first += 1
            while s[first] not in counter_t:
                first += 1
            if min_window_size > last - first + 1:
                min_window_size = last - first + 1
                min_window_first = first
                min_window_last = last

        return s[min_window_first : min_window_last + 1]
