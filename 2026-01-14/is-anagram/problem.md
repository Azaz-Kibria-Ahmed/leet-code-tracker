  
NeetCode 150
Pro
Question
Solution
Submissions
Submission	Language	Code	Analysis


Accepted

01/14/2026

	Python	
View
	
Analyze Complexity



Accepted

01/14/2026

	Python	
View
	
Analyze Complexity



Accepted

01/14/2026

	Python	
View
	
Analyze Complexity



Accepted

01/14/2026

	Python	
View
	
Analyze Complexity



Accepted

01/14/2026

	Python	
View
	
Analyze Complexity



Accepted

01/14/2026

	Python	
View
	
Analyze Complexity



Accepted

01/14/2026

	Python	
View
	
Analyze Complexity



Accepted

01/14/2026

	Python	
View
	
Analyze Complexity



Accepted

01/14/2026

	Python	
View
	
Analyze Complexity



Accepted

01/14/2026

	Python	
View
	
Analyze Complexity



Accepted

01/14/2026

	Python	
View
	
Analyze Complexity



Accepted

01/14/2026

	Python	
View
	
Analyze Complexity



Accepted

01/14/2026

	Python	
View
	
Analyze Complexity



Accepted

01/14/2026

	Python	
View
	
Analyze Complexity



Accepted

10/01/2025

	Python	
View
	
Analyze Complexity



Accepted

09/27/2025

	Python	
View
	
Analyze Complexity
Python
Solution 1
+
Hint
|
|
Ln 1, Col 1
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        if len(s) != len(t):
            return False
        s_counts = {} #A hash set only tells you if a character exists, not how many times it exists. Anagrams must have the exact same count for each character.
        t_counts = {}
        for char in s:
    
            if char in s_counts:
                s_counts[char] = s_counts[char] + 1 #foro loop#1, loop through first string to count characters
            else:
                s_counts[char] = 1
  
        for char in t:
    
            if char in t_counts:
                t_counts[char] = t_counts[char] + 1
            else:
                t_counts[char] = 1     # for loop#2, loop through second string to count characters
        return s_counts == t_counts# see if both dicionaries are equal
Test Case
Output
Case 1Case 2

s =

t =

Console  