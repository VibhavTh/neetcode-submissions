class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        #knowing we have max 3 different elements we could use 3 write pointers for each color and somehow have a rule on when to switch curr element with some pointer to enforce the sort rule


        #we have 3 sections that we need to sort to essentially 3 buckets:
        #  0s   |     1s      |     2s


        # 0 1 0 1 1 2 0 2 2

    # #count num of 0, 1, 2s in first pass. still 0(1) space complexity since fixed size
    #     count = [0] * 3

    #     for num in nums:
    #         count[num] += 1
    
    # #then recounstruct it second pass with global index and while loop to reach end of every bucket
    #     j = 0
    #     for i in range(3):
    #         while count[i] != 0:
    #             nums[j] = i
    #             count[i] -= 1
    #             j += 1
        


        l, r = 0, len(nums) - 1
        i = 0

        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        while i <= r:
            if nums[i] == 0:
                swap(i, l)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                continue

            #case 0 after left swap or 1
            i += 1

# 0 1 2 1 0 2
