class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #heap solution with freq map and min heap
        #heap of freq, values using tuple always remember when we need to use a data structure but need to keep track of multiple things like in this case frequency and value then we can use a tuple and sort by first element


        freq = {}
        min_heap = []
        res = []
        
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        

        for val, frequency in freq.items():
            heapq.heappush(min_heap, (frequency, val))

            if len(min_heap) > k:
                heapq.heappop(min_heap)
                
        
        for i in range(k):
            cur = heapq.heappop(min_heap)
            res.append(cur[1])
        
        return res


            