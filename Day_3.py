# Functions
'''
1.arg pass return value

2.arg pass no return value

3.no arg no return 

4.no arg return value
'''

#no arg no return
'''
def hi(): #Callee
    print("Hello")
    print("Students.....",end=" ")
    print("Good Morning")
hi() #Caller 
'''

#arg pass no return type
'''
def summate(a,b):
    sum=a+b
    print("Sum :",sum)
    
def difference(a,b):
    diff=a-b
    print("Difference :",diff)
    
a=int(input())
b=int(input())
summate(a,b)
difference(a,b)
'''        
 
#no arg but return value(It return output from caller (Out of the function))
'''
def addition():
    a=int(input())
    b=int(input())
    c=a+b
    return c
summate=addition() #OUT OF THE FUNCTION #CALLER
print(summate)
'''

#arg pass and return value 
'''
def expo(a,b):
    return a**b
x=int(input("Enter x: "))
y=int(input("Enter y: "))
res=expo(x,y)
print("Result :",res)   
'''   

#Recursions

'''
A Function solving a problem by breaking it into smaller same problems 

There are 2 imp components of recursion 

1.Base Case --> Stooping Condition / Prevents infinte calls

2.Recursive Case --> Function calls iself with smaller or larger input

Types of Recursion :

1) DIRECT RECURSION

2)INDIRECT RECURSION

3)HEAD RECURSION 

4)TAIL RECURSION

5)TREE RECURSION

6)NESTED RESURSION

7)LINEAR RECURSION

'''
# DIRECT RECURSION
''' 
def nums(n):
    if n==0:
        return 
    print(n,end=" ")
    nums(n-1)
n=int(input())
nums(n)   
'''
'''
def nums(n):
    if n==10:
        print(10)
        return 
    print(n,end=" ")
    nums(n+1)
n=int(input())
nums(n)  
'''

#INDIRECT RECURSION
'''
def func_A(n):
    if n<=0:
        return 
    print("A :",n)
    func_B(n-1)
def func_B(n):
    if n<=0:
        return 
    print("B :",n)
    func_A(n-1)
n=int(input())    
func_A(n)        
'''

'''
def is_even(n):
    if n<=0:
        return True
    return is_odd(n-1)
def is_odd(n):
    if n<=0:
        return False
    return is_even(n-1)
n=int(input())
if is_even(n):
    print("Even")
else:
    print("Odd")    
'''

#NESTED RECURSION
'''
n=int(input())
print(func(n))

def func(n):
    if n>10:
        return n-1
    return func(func(n+2))
'''    
'''
func(func(7))
func(func(func(9)))
func(func(func(func(11))))
func(func(func(10)))
func(func(9))
func(func(func(11)))
func(func(10))
func(9)
func(func(11))
func(10)
func(func(12))
func(11)
10
'''
