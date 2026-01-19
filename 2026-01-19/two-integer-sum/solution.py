class Solution:

    def twoSum(self, nums, target):  # EXAMPLE nums = [4,5,6] target = 11

        seen_numbers = {} #make a Dictionary ; at some point Dictionary will look like this {4:0, 5:1}, in this case currently looking at numner 6

        for current_index, current_num in enumerate(nums): #this line ensures that we go through Dictionary and look for the current_index & current_num
            complement = target - current_num # complement = 11 - 6 --> Complement = 5
            if complement in seen_numbers: #Check if the complement number "5" is in Dictionary
                return [seen_numbers[complement], current_index] # "YES" it is! the return statement looks up seen_number[5]. The Dictionary returns value for Key 5, which is Index 1. It also takes the current Index "2". Therefore combines iin a list and returns [1,2]
            seen_numbers[current_num] = current_index 

    

      
        
      #i != j
      #nums = array of Integers
      #target = integer
      #return indices i & j such that nums [i] + nums[j] == target  

      #so output = nums [i] + nums [j] == target
      # E.X --> nums = [4,5,6], target = 10, therefore output will be = [0,2]
      # We can use the bruteforce method, to find output, but only problem will be that it will give a time complexity of O(n^2),
      #But what if we change the equation around from nums[i] + nums[j] == target to ---> nums[i] == target - nums[j]
      #nums[i] == target - nums[j] --> when we're at nums[0], whihc is (2), we need to find it's partner --> nums[i] = 9 - 2 --> 7 = 9 - 2 (assuming the way we re-aranged this problem is that if the [aerson inputs the target number it goes to the first index and subtracts that from the target and if the number is avilable within the array then that is the value of our second number? confirm])
      #Hash-map is a quicker process because it goes through the array once, where as a the brute force method we would be going through the array again in order to find the target number
      #so using the hash-map method, we essentally keep building the hash-map array with the current number and it's index until we find our partner number? So the hash -map keeps on getting bigger until we find the partner number and from there we can return the two two indices from the initial nums array as the output?
      #Let's trace our example: nums = [2, 7, 11, 15], target = 9.

##Start: seen_map is empty: {}. We look at the first number, 2.

#Number = 2 (at index 0):

#We need a partner: complement = target - num which is 9 - 2 = 7.

#heck the map: Is 7 in our seen_map? No, the map is empty.

#Since we didn't find the partner, let's add the current number (2) and its index (0) to the map.

#seen_map is now: {2: 0}.

#Number = 7 (at index 1):

#We need a partner: complement = 9 - 7 = 2.

#Check the map: Is 2 in our seen_map? YES! It is.

#We found it! The partner's value is 2, and its index is seen_map[2], which is 0. The current number is 7, and its index is 1.

#We can immediately return the two indices: [0, 1].


      
      
      
      
      
      
      
      
    