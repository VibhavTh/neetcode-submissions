class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        minVal = float('inf')
        pivot = 0

        #split into two sorted arrays at the pivot point and do binary search 

        while l < r:

            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            
            else:
                r = m

        pivot = r
        print(pivot)
        #if in right sorted
        if target >= nums[pivot] and target <= nums[-1]:
            l = pivot
            r = len(nums) - 1
        #else its in left sorted
        else:
            l = 0
            r = pivot - 1


        print(l, r)

        while l <= r:
            m = (l + r) // 2
            
            if target == nums[m]:
                return m
            
            elif target > nums[m]:
                l = m + 1
            
            else:
                r = m - 1
        
        return -1

                    

        