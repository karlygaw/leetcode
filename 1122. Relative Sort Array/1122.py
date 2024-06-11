class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        new_arr = []
        new_arr2 = []
        for i in arr2:
            new_arr.extend([i] * arr1.count(i))
        for i in arr1:
            if i not in arr2:
                new_arr2.append(i)
        new_arr.extend(sorted(new_arr2))
        return new_arr
