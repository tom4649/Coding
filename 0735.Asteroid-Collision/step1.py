class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        asteroids_moving_left = []
        asteroids_moving_right = []
        for asteroid in asteroids:
            if asteroid > 0:
                asteroids_moving_right.append((asteroid, len(asteroids_moving_left)))
            else:
                while asteroids_moving_right and asteroids_moving_right[-1][0] < abs(
                    asteroid
                ):
                    asteroids_moving_right.pop()
                if asteroids_moving_right and asteroids_moving_right[-1][0] == abs(
                    asteroid
                ):
                    asteroids_moving_right.pop()
                    continue
                if not asteroids_moving_right:
                    asteroids_moving_left.append(asteroid)

        result = []
        index_moving_right = 0
        for i in range(len(asteroids_moving_left) + 1):
            while index_moving_right < len(asteroids_moving_right) and (
                i == len(asteroids_moving_left)
                or i >= asteroids_moving_right[index_moving_right][1]
            ):
                asteroid, _ = asteroids_moving_right[index_moving_right]
                result.append(asteroid)
                index_moving_right += 1
            if i < len(asteroids_moving_left):
                result.append(asteroids_moving_left[i])

        return result
