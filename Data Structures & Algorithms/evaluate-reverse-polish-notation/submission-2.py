class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i not in '+-*/':
                stack.append(i)
            elif i == "+":
                a=stack.pop()
                b=stack.pop()
                stack.append(int(a)+int(b))
            elif i == "-":
                b=stack.pop()
                a=stack.pop()
                stack.append(int(a)-int(b))
            elif i == "*":
                b=stack.pop()
                a=stack.pop()
                stack.append(int(a)*int(b))
            elif i == "/":
                b=stack.pop()
                a=stack.pop()
                stack.append(int(a)/int(b))
        print(stack)
        return int(stack[-1])
        