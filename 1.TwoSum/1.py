class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} # key: value -> number:index
        
        for i in range(len(nums)): 
            diff = target - nums[i] 
            
            if diff in hashMap:
                return [hashMap[diff], i]
            else:
                hashMap[nums[i]] = i
        return []