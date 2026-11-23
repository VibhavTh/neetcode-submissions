class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #o(n) time o(1) space - in place

        #brute force n^2 iterate thru each loop per new value

        #using dict as freq map o(n) time with o(n) space


        # freq = {}

        # for num in nums:
        #     freq[num] = freq.get(num, 0) + 1

        #     #know we have a majority and can return first occurance
        #     if freq[num] > len(nums) // 2:
        #         return num



        # boyer moore algorithm o(n) time o(1) space because we r given a majority element


        count, res = 0, nums[0]

        for n in nums:

            if n == res:
                count += 1

            if n != res:
                count -= 1

            if count == 0 and n != res:
                res = n
                count = 1
        
        return res

