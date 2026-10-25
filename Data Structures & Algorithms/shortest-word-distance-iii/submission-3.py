class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        positions = {}
        res = float('inf')

        for index, word in enumerate(wordsDict):
            if word not in positions:
                positions[word] = []
            positions[word].append(index)


        i, j = 0, 0
        pos1, pos2 = positions.get(word1), positions.get(word2)

        if word1 == word2:
            j = 1
            while j < len(pos1):
                res = min(res, abs(pos1[i] - pos1[j]))
                i += 1
                j += 1
        else:
            while i < len(pos1) and j < len(pos2):
                res = min(res, abs(pos1[i] - pos2[j]))
                
                if pos1[i] < pos2[j]:
                    i += 1
                else:
                    j += 1

        return res
