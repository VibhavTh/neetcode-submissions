class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #area = min(height) * width
        #we use a greedy algorithm optimizing area as we traverse axross the height array with two pointers
        #keep track of max area with max() function

        #use a while loop until we run out of valid combinations to check 

        l, r = 0, len(heights) - 1
        res = 0

        while l <= r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)

            if heights[l] < heights[r]:
                l += 1
            
            else:
                r -= 1
        
        return res