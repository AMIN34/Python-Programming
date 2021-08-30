class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)-1):
            if nums[i]==target:
                return i
        nums.append(target)
        nums.sort()
        return nums.index(target)