class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                #print(i, j)
                if target == nums[i] + nums[j]:
                    return list([i, j])
