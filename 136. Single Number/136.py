class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        element_counts = Counter(nums)
        single_occurrence = [element for element, count in element_counts.items() if count == 1]
        return single_occurrence[0]