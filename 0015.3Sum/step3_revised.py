class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sorted_nums = sorted(nums)
        result = []

        for i in range(len(sorted_nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            start = i + 1
            end = len(sorted_nums) - 1
            while start < end:
                total = sorted_nums[i] + sorted_nums[start] + sorted_nums[end]
                if total == 0:
                    result.append(
                        [sorted_nums[i], sorted_nums[start], sorted_nums[end]]
                    )
                    start += 1
                    end -= 1
                    while start < end and sorted_nums[start] == sorted_nums[start - 1]:
                        start += 1
                    while start < end and sorted_nums[end] == sorted_nums[end + 1]:
                        end -= 1
                elif total > 0:
                    end -= 1
                else:
                    start += 1

        return result


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sorted_nums = sorted(nums)
        result = []

        for i in range(len(sorted_nums) - 1):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            seen = set()
            j = i + 1
            while j < len(sorted_nums):
                diff = -(sorted_nums[i] + sorted_nums[j])
                if diff in seen:
                    result.append([sorted_nums[i], diff, sorted_nums[j]])
                    while (
                        j < len(sorted_nums) - 1
                        and sorted_nums[j] == sorted_nums[j + 1]
                    ):
                        j += 1
                seen.add(sorted_nums[j])
                j += 1

        return result
