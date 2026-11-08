import collections

EMPTY = 0
BUILDING = 1
OBSTACLE = 2

def shortest_distance_from_all_buildings(grid: list[list[int]]) -> int:
    if not grid or not grid[0]:
        return -1

    m = len(grid)
    n = len(grid[0])
    sum_of_distance = [[0] * n for _ in range(m)]
    num_reached = [[0] * n for _ in range(m)]

    def traverse(r_start, c_start):
        visited = set()
        to_visit = collections.deque([(r_start, c_start, 0)])

        while to_visit:
            r, c, distance = to_visit.popleft()
            for r_next, c_next in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if not (0 <= r_next < m and 0 <= c_next < n):
                    continue
                if grid[r_next][c_next] != EMPTY or (r_next, c_next) in visited:
                    continue
                to_visit.append((r_next, c_next, distance + 1))
                visited.add((r_next, c_next))
                sum_of_distance[r_next][c_next] += distance + 1
                num_reached[r_next][c_next] += 1

    num_buildings = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == BUILDING:
                num_buildings += 1
                traverse(r, c)

    possible_shortest_distances = [sum_of_distance[r][c] for r in range(m) for c in range(n) if num_reached[r][c] == num_buildings]

    return min(possible_shortest_distances) if possible_shortest_distances else -1


if __name__ == "__main__":
    grid = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = shortest_distance_from_all_buildings(grid)
    print(res)



# Your previous Plain Text content is preserved below:

# This is just a simple shared plaintext pad, with no execution capabilities.

# When you know what language you'd like to use for your interview,
# simply choose it from the dots menu on the tab, or add a new language
# tab using the Languages button on the left.

# You can also change the default language your pads are created with
# in your account settings: https://app.coderpad.io/settings

# Enjoy your interview!
