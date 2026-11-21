class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for i in range(len(s)):
            if (s[i].isalnum()):
                new_s += s[i].lower()
        reverse_new_s = new_s[::-1]
        if (new_s == reverse_new_s):
            return True
        else:
            return False



        