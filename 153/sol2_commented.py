class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            raise ValueError("The input list is empty.")
        left = 0
        right = len(nums)
        pivot = nums[0]

        # flags = [n < pivot for n in nums]
        # [False, ... False, True, ... True]
        # ループ不変条件: i < left -> flags[i] is False && i >= right -> flags[i] is True (1)
        # ループ停止条件: left >= right (2)
        # ループ事後条件: left == right  && i < left -> flags[i] is False && i >= right -> flags[i] is True
        # True が一つも存在しない場合の場合分けが必要
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= pivot:
                left = mid + 1
            else:
                right = mid

        return nums[left] if left < len(nums) else pivot
