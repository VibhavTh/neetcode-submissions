class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        #binary search over the range from 1 - max(piles) of eating speeds to see most optimal eating speed
        # try each eating speed and if it works set it to return variable with min function for optimality 
        
        def trying(piles, speed, h):
            count = 0
            for pile in piles:
                if pile:
                    count += math.ceil(pile / speed) 
                if count > h:
                    return -1
            
            return count 

        res = max(piles)
        minSpeed = float('inf')

        l = 1 
        r = max(piles)

        while l <= r:
            mid = (l + r) // 2
            attempt = trying(piles, mid, h)
            print(mid, attempt)
            if attempt == -1:
                l = mid + 1
            else:
                if attempt <= minSpeed or mid < res:
                    minSpeed = attempt
                    res = mid
                r = mid - 1

        return res
            


