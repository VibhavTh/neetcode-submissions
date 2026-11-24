class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        #knowing we have max 3 different elements we could use 3 write pointers for each color and somehow have a rule on when to switch curr element with some pointer to enforce the sort rule


        #we have 3 sections that we need to sort to essentially 3 buckets:
        #  0s   |     1s      |     2s

        #we set rules that 0's low and 2's high bounderies and 1s is where current should be in middle
        #swap 

        # 0 1 0 1 1 2 0 2 2

    #count num of 0, 1, 2s in first pass. still 0(1) space complexity since fixed size
        count = [0] * 3

        for num in nums:
            count[num] += 1
        
        j = 0
        for i in range(3):
            while count[i] != 0:
                nums[j] = i
                count[i] -= 1
                j += 1
        



