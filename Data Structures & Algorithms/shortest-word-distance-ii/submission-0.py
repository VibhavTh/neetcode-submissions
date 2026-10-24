class WordDistance:

    #initalizes locations with freq map of list of indexes where word is in wordDict
    def __init__(self, wordsDict: List[str]):
        self.locations = defaultdict(list)
        
        for index, word in enumerate(wordsDict):
            self.locations[word].append(index)
            

        

    def shortest(self, word1: str, word2: str) -> int:
        pos1, pos2 = self.locations.get(word1), self.locations.get(word2)
        res = float('inf')

        print(pos1, pos2)

        if len(pos1) == 1 and len(pos2) == 1:
            return abs(pos1[0] - pos2[0])
        

        
        l1, l2, n1, n2 = 0, 0, len(pos1), len(pos2)
        print(pos1[l1], pos2[l2])

        while l1 < n1 and l2 < n2:
            res = min(res, abs(pos1[l1] - pos2[l2]))

            if (l1 + 1) < n1 and (l2 + 1) < n2:
                if pos1[l1 + 1] < pos2[l2 + 1]:
                    l1 += 1
                else:
                    l2 += 1
            
            else:
                if (l1 + 1) < n1:
                    l1 += 1
                else:
                    l2 += 1

        return res


        #[4, 9]  #[1, 7]
        # the list of indexes will be in order 
        #have two lists need to find shortest distance between them kind of like container with most water problem

        # [practice, coding, practice, practice, makes, practice, practice coding, practice, makes]
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
