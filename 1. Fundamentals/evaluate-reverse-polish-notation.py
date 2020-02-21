class Solution:
    
    def getSum(op, num1, num2): #lol what a punny name
        if op == "+":
            return num1 + num2
        if op == "-":
            return num1 - num2
        if op == "*":
            return num1 * num2
        if op == "/":
            return num1 / num2
        
        
    def isOperator(token):
        return token in ["+","-","*","/"]
                
                
    def evalRPN(self, tokens: List[str]) -> int:
        myStack = [] 
        for token in tokens:
            myStack.append(token)
            if isOperator(token):
                op = tokens.pop()
                item2 = tokens.pop()
                item1 = tokens.pop()
                sum = getSum(op, item1, item2)
                myStack.append(sum)
        return myStack[0]