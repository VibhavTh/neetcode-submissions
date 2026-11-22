class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = {}

        #if nums[i] - 1 in dict then we know its part of a sequence if not treat it as the beginning of a new sequence

        #

        nums = set(nums)
        count = 1

        if not nums:
            return 0

        for n in nums:
            check = 1
            #beginning of sequence
            if n - 1 not in nums:
                while n + 1 in nums:
                    n = n + 1
                    check += 1
                
                count = max(count, check)
            
        return count

    

        