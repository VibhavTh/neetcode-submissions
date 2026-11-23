class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        #create dict/hashmap where key = anagram signature and value = list of strings with same anagram signature

        #we can find the anagram signature by getting all possible letters and creating a frequency map for each string and that frequency map is the signature

        #ex: "abc"  a = 1, b = 1, c = 1, every other letter = 0

        #we need to create a list initally to mutate the freq map till we reach end of current string then convert it into a tuple to store it in the dict as a key 

        for s in strs:
            signature = [0 for _ in range(26)]

            for c in s:
                index = ord(c) - ord('a')
                signature[index] += 1       

            groups[tuple(signature)].append(s)
    
        return list(groups.values())

        

        