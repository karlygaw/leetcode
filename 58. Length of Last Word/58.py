class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # lines = s.splitlines()
        # if lines:
        #     last_line = lines[-1]
        #     start_index2 = s.rfind(last_line)
        res = s.split()
        return len(res[-1])