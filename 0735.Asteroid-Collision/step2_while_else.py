class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for asteroid in asteroids:
            while asteroid < 0 and stack and stack[-1] > 0:
                if stack[-1] == abs(asteroid):
                    stack.pop()
                    break
                elif stack[-1] < abs(asteroid):
                    stack.pop()
                else:
                    break
            else:
                stack.append(asteroid)

        return stack
