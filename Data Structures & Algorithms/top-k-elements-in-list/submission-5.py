class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #heap of freq, values using tuple 
        freq = {}
        min_heap = []
        res = []
        
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        

        for val, frequency in freq.items():
            heapq.heappush(min_heap, (-frequency, val))
        
        while k != 0:
            cur = heapq.heappop(min_heap)
            res.append(cur[1])
            k -= 1
        
        return res
            