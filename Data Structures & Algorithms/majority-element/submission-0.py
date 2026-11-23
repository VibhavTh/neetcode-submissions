class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #o(n) time o(1) space - in place

        #brute force n^2 iterate thru each loop per new value

        #using dict as freq map o(n) time with o(n) space

        #


        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
            if freq[num] > len(nums) // 2:
                return num





