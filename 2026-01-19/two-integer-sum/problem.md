  
NeetCode 150
Pro
Question
Solution
Submissions
Two Sum
Solved 
Easy
Company Tags
Hints

Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]

Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:

Input: nums = [4,5,6], target = 10

Output: [0,2]

Example 3:

Input: nums = [5,5], target = 10

Output: [0,1]

Constraints:

2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000
Only one valid answer exists.



Recommended Time & Space Complexity


Hint 1


Hint 2


Hint 3


Company Tags
Build Customer-Aware AI Agents
Query user attributes with 45ms response times through a secure, scalable API designed for applications and AI agents
Download Free
Share Carbon Ad Icon
Copy Link
Send via email
Refresh Carbon Ad
ads via Carbon
Python
Solution 1
+
Hint
|
|
Ln 1, Col 1
23
24
25
26
27
28
29
30
31
32
33
22
21
20
19
18
17
16
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
      # E.X --> nums = [4,5,6], target = 10, therefore output will be = [0,2]
      # We can use the bruteforce method, to find output, but only problem will be that it will give a time complexity of O(n^2),
      #But what if we change the equation around from nums[i] + nums[j] == target to ---> nums[i] == target - nums[j]
      #nums[i] == target - nums[j] --> when we're at nums[0], whihc is (2), we need to find it's partner --> nums[i] = 9 - 2 --> 7 = 9 - 2 (assuming the way we re-aranged this problem is that if the [aerson inputs the target number it goes to the first index and subtracts that from the target and if the number is avilable within the array then that is the value of our second number? confirm])
      #Hash-map is a quicker process because it goes through the array once, where as a the brute force method we would be going through the array again in order to find the target number
      #so using the hash-map method, we essentally keep building the hash-map array with the current number and it's index until we find our partner number? So the hash -map keeps on getting bigger until we find the partner number and from there we can return the two two indices from the initial nums array as the output?
      #Let's trace our example: nums = [2, 7, 11, 15], target = 9.
##Start: seen_map is empty: {}. We look at the first number, 2.
#Number = 2 (at index 0):
      #so output = nums [i] + nums [j] == target
      #return indices i & j such that nums [i] + nums[j] == target  
      #target = integer
      #nums = array of Integers
      #i != j
        
      
    
            seen_numbers[current_num] = current_index 
                return [seen_numbers[complement], current_index] # "YES" it is! the return statement looks up seen_number[5]. The Dictionary returns value for Key 5, which is Index 1. It also takes the current Index "2". Therefore combines iin a list and returns [1,2]
            if complement in seen_numbers: #Check if the complement number "5" is in Dictionary
            complement = target - current_num # complement = 11 - 6 --> Complement = 5
        for current_index, current_num in enumerate(nums): #this line ensures that we go through Dictionary and look for the current_index & current_num
        seen_numbers = {} #make a Dictionary ; at some point Dictionary will look like this {4:0, 5:1}, in this case currently looking at numner 6
    def twoSum(self, nums, target):  # EXAMPLE nums = [4,5,6] target = 11
class Solution:
Test Case
Output
Case 1Case 2

nums =

target =

Console  