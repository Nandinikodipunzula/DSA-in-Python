class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloonCounter = [0]*26
        txtCounter = [0]*26
        for char in 'balloon':
            balloonCounter[ord(char)-ord('a')]+=1
        for char in text:
            txtCounter[ord(char)-ord('a')]+=1
        maxBallons = float("inf")
        for char in 'balloon':
            bFreq = balloonCounter[ord(char)-ord('a')]
            tFreq =  txtCounter[ord(char)-ord('a')]
            maxBallons = min(maxBallons , tFreq // bFreq)
        return maxBallons
        
if __name__ == "__main__":    
    solution = Solution()
    maxBallons = solution.maxNumberOfBalloons('baaalllloooonnaaabbb')
    print(maxBallons)   