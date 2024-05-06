class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patternLen = len(pattern)
        words = s.split(" ")

        if patternLen != len(words):
            return False
        
        wordToChar = {}
        charToWord = {}

        for char, word in zip(pattern,words):
            if char in charToWord and charToWord[char]!=word:
                return False
            if word in wordToChar and wordToChar[word]!=char:
                return False
            wordToChar[word]=char
            charToWord[char]=word
            
        return True
    
if __name__ == "__main__":    
    solution = Solution()
    isSamePattern = solution.wordPattern('aaaa','dog cat cat dog')
    print(isSamePattern)  

    isSamePattern = solution.wordPattern('abba','dog cat cat dog')
    print(isSamePattern)  
            
            



        