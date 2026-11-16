class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = {}
        if len(s) != len(t):
            return False
        for letter in s:
            if (map_s.get(letter)):
                map_s[letter] += 1
            else:
                map_s[letter] = 0
        map_j = {}
        for letter in t:
            if (map_j.get(letter)):
                map_j[letter] += 1
            else:
                map_j[letter] = 0 
        if (map_s == map_j):
            return True
        else:
            return False
