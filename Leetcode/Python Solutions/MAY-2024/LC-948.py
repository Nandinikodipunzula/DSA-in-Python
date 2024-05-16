class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int: 
        low = 0
        high = len(tokens)-1
        score = 0
        if len(tokens) == 0 : 
            return 0
        if len(tokens) == 1 and tokens[0] <=power :
            return 1
        if len(tokens) == 1 and tokens[0] > power :
            return 0
        tokens.sort()

        while low <= high :
            if power >= tokens[low]:
                power-=tokens[low]
                score+=1
                low+=1
                continue
            else:
                if score >=1 and high-low > 1:
                    power+=tokens[high]
                    score-=1
                    high-=1
                else: break
        return score




        
        