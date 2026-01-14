class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        if len(s) != len(t):
            return False

        s_counts = {} #A hash set only tells you if a character exists, not how many times it exists. Anagrams must have the exact same count for each character.
        t_counts = {}

        for char in s:
    
            if char in s_counts:
                s_counts[char] = s_counts[char] + 1 #foro loop#1, loop through first string to count characters
            else:
                s_counts[char] = 1
  
        for char in t:
    
            if char in t_counts:
                t_counts[char] = t_counts[char] + 1
            else:
                t_counts[char] = 1     # for loop#2, loop through second string to count characters

        return s_counts == t_counts# see if both dicionaries are equal