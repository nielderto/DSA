# Given an array = [2, 5, 1, 2, 3, 5, 1, 2, 4]
# Output: 2

# Given an array = [2, 1, 1, 2, 3, 5, 1, 2, 4]
# Output: 1

# Given an array = [2, 3, 4, 5]
# Output: Undefined


class Solution:
    def firstReccuringChar(self, nums):
        count = {}
        for i in range(0, len(nums)):
            if nums[i] in count:
                return nums[i]
            count[nums[i]] = i
        return "Undefined"
    

s = Solution()
print(s.firstReccuringChar([2, 5, 1, 2, 3, 5, 1, 2, 4])) # Output: 2
print(s.firstReccuringChar([2, 1, 1, 2, 3, 5, 1, 2, 4])) # Output: 1
print(s.firstReccuringChar([2, 3, 4, 5]))
