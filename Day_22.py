#
'''
Precedence
**
^
()
/ * % //

'''

#Check balance of paranthesis
'''
s = input("Enter the Expression : ")
stack = []
valid = True

for ch in s:
    if ch in '({[':
        stack.append(ch)

    elif ch in ')}]':
        if len(stack) == 0:
            valid = False
            break

        top = stack.pop()

        if (ch == ')' and top != '(') or \
           (ch == '}' and top != '{') or \
           (ch == ']' and top != '['):
            valid = False
            break

if len(stack) != 0:
    valid = False

if valid:
    print("Balanced")
else:
    print("Not Balanced")
'''

#Balance the parathesis
 
'''
s=input("Enter an Expression:")
stack=[]
result=""
for ch in s:
    if ch=='(':
        stack.append(ch)
        result+=ch
    elif ch==')':
        if len(stack)>0:
            stack.pop()
            result+=ch
        else:
            result='('+result+')'
while len(stack)>0:
    result+=')'
    stack.pop()
print("Balanced",result)
'''

#Infix Expression to Postfix Conversion

'''
s=input("Enter the Expression: ")
stack=[]
result=""
priority={'+':1,'-':1,'*':2,'/':2}
for ch in s:
    if ch.isalnum():
        result+=ch
    elif ch=='(':
        stack.append(ch)
    elif ch==')':
        while stack and stack[-1]!='(':
            result+=stack.pop()
        stack.pop()
    else:
        while stack and stack[-1]!='(' and priority[ch]<=priority[stack[-1]]:
            result+=stack.pop()
        stack.append(ch)
while stack:
    result+=stack.pop()
print("Postfix Expression:",result)    
'''

#Infix to Postfix Evaluatiion

'''
s=input("Enter the infix Expression: ")
stack=[]
for ch in s:
    if ch.isdigit():
        stack.append(int(ch))
    else:
        b=stack.pop()
        a=stack.pop()
        if ch=='+':stack.append(a+b)
        elif ch=='-':stack.append(a-b)
        elif ch=='*':stack.append(a*b)
        elif ch=='/':stack.append(a/b)    
print("Result",stack[0])
'''
#Prefix Conversion

s=input("Enter the infix Expression: ")[::-1]
stack=[]
for ch in s:
    if ch.isdigit():
        stack.append(int(ch))
    else:
        b=stack.pop()
        a=stack.pop()
        if ch=='+':stack.append(a+b)
        elif ch=='-':stack.append(a-b)
        elif ch=='*':stack.append(a*b)
        elif ch=='/':stack.append(a/b)    
print("Result",stack[0])






















                  