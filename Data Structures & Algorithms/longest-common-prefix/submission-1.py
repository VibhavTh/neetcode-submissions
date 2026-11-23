class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        min_length = len(min(strs))
        
        for i in range(min_length):
            for s in strs:
                if s[i] != strs[0][i]:
                    return prefix
                
            prefix += strs[0][i]

        return prefix