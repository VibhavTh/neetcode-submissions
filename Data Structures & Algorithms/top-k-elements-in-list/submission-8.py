class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #heap solution with freq map and min heap
        #heap of freq, values using tuple always remember when we need to use a data structure but need to keep track of multiple things like in this case frequency and value then we can use a tuple and sort by first element


        # freq = {}
        # min_heap = []
        # res = []
        
        # for num in nums:
        #     freq[num] = freq.get(num, 0) + 1
        

        # #can either use a min heap and keep track of size of min heap so in the end the the minheap only holds the results of top k frequent elements 
        # #or use a max heap store all elements then heappop top k but its slightly less efficient and elegant

        # for val, frequency in freq.items():
        #     heapq.heappush(min_heap, (frequency, val))

        #     if len(min_heap) > k:
        #         heapq.heappop(min_heap)
                
        
        # for i in range(k):
        #     cur = heapq.heappop(min_heap)
        #     res.append(cur[1])
        
        # return res


        count = {}
        freq = [[] for i in range(len(nums) + 1)] # index is frequency and value is list of elements having that frequency
        res = []

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for value, frequency in count.items():
            freq[frequency].append(value)

        
        #we need to go backwards in the freq array to get top K freq elements
        for i in range(len(freq) - 1, -1, -1):
            for j in range(len(freq[i])):
                res.append(freq[i][j])
                if len(res) == k:
                    return res



            