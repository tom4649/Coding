from bisect import bisect_left, bisect_right

a = [1, 3, 5]
print(bisect_left(a, 2))  # 1
print(bisect_left(a, 3))  # 1
print(bisect_right(a, 3))  # 2
