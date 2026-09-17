class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26;
            for c in s:
                #adds 1 to value of ord of letter subtracted by a to its corresponding index 0-26 in count
                count[ord(c)- ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
        