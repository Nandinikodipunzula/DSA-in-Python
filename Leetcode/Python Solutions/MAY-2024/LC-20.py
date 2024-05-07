from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        #can directly be modified as stack = []
        #but I read there will be memory issues of stack grows long
        parentheses = {}
        parentheses[')'] = '('
        parentheses['}'] = '{'
        parentheses[']'] = '['
        
        for char in s:
            if  char in '({[]})':
                if char in '({[':
                    stack.append(char)
                elif char in ']})':
                    if len(stack)<=0 or parentheses[char]!= stack[-1]:
                        return False
                    stack.pop()
        return len(stack)==0
            
        