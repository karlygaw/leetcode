class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''
        for i in range(len(s)):
            if s[i].isalpha():
                new_s += s[i].lower()
            elif s[i].isdigit():
                new_s += s[i]
            else:
                continue
        print(new_s)
        if new_s == new_s[::-1]:
            return True
        else:
            return False