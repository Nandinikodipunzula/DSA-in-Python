class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=" ".join(s.strip().split(" "))
        words=s.split(" ")
        return len(words[len(words)-1])
    
    def lengthOfLastWord2(self, s: str) -> int:
        i , length = len(s)-1,0
        characterSeen = False
        while i >= 0 :
            if s[i] == " " and characterSeen == False:
                continue
            elif s[i]!= " " and s[i].isalpha():
                length+=1
                characterSeen = True
            elif  s[i] == " " and characterSeen == True:
                return length
            i-=1
        return length


            
if __name__ == "__main__":
    obj=Solution()
    result = obj.lengthOfLastWord2("I will                master      python                     sooonnnnnnn")
    print(result)