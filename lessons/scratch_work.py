class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result: list[int] = []
        i: int = 0
        while i < len(nums):
            alt_i = i + 1 
            while alt_i < len(nums):
                if nums[i] + nums[alt_i] == target:
                    result.append(i)
                    result.append(alt_i)
                
                alt_i += 1
            i += 1

        return result

nums: list[int] = [300,100,200,200]
target: int = 400
obj_1 = Solution()

print(obj_1.twoSum(nums, target))