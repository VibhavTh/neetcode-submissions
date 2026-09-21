class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        
        minVal = float('inf')

        while l <= r :
            m = (l + r) // 2
            print(m)
            if nums[m] > nums[r]:
                l = m + 1
            else:
                minVal = min(minVal, nums[m])
                r = m - 1
            

        
        return minVal