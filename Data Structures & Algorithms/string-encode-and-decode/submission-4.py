class Solution:

    def encode(self, strs: List[str]) -> str:
        #strs = ["Hello","World"] -> "5#Hello5#World"
        #length-prefix encoding 
        #we need length and special symbol to differntiate between integer and special symbol characters edge cases

        encoded_string = []

        for s in strs:
            encoded_string.append(str(len(s)))
            encoded_string.append("#")
            encoded_string.append(s)
        
        print(encoded_string)
        return "".join(encoded_string)


        
    def decode(self, s: str) -> List[str]:
        #strs = "Hello World" -> ["Hello","World"] 

        #when we get to empty space create new word 

        decoded_string = []
        i = 0

        while i < len(s):
            j = i

            #need to check for lengths above 9
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            i = j + 1
            decoded_string.append(s[i:length + i])

            i += length
        
        return decoded_string

