class Solution:
    def compress(self, chars: List[str]) -> int:
        # so two pointer, sliding window technique where:
        # r += 1 every iteration 
        # l = r when r reaches a new char or end of the group 
        # we calculate group length by doing len = r - l + 1 since 0 indexing
        # then we check if len > 10:
        # example len = 423 we need to split into 4, 2, and 3 
        # 42 % 10 = 2, 42 // 10 = 4 
        # so we use while loop with len % 10 to get last digit, len // 10 to get first digit until there's no more digits to split
        #get value from left pointer + group len digit(s)
        
        #base case
        #if len == 1:
        #   move left pointer to right and continue
        
        #else:
        #   for i in range(len):
        #       l += 1
        #       chars[l] = digits[i]
        #   l == r and continue

        k, i = 0, 0
        n = len(chars)

        while i < n:
            chars[k] = chars[i]
            k += 1
            j = i + 1

            while j < n and chars[j] == chars[i]:
                j += 1
            
            group = j - i
            if group > 1:
                for c in str(group):
                    chars[k] = c
                    k += 1
            i = j
        
        #k is where we finished modifying the 
        return k 



            
            
