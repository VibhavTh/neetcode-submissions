class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        #assume array is linked list and we need to find a
        #cycle in the DAG 

        # 1 - 4 - 2 - 3 
        #         |   |
        #         - - -
        
        # 0 1 2 3 4 
        # 1 4 2 3 2

        
        fast, slow = 0, 0
        

        while True: 
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break


        slow2 = 0

        while slow2 != slow:
            slow = nums[slow]
            slow2 = nums[slow2]

        
        return slow