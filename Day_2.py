#Armstrong number
'''
n=input("Enter a Number: ")
temp=int(n)
l=len(n)
n=int(n)
sum=0

while n>0:
    digit=n%10
    sum+=digit**l
    n=n//10
if temp==sum:
    print("Armstrong")
else:
    print("Not an Armstrong number")
'''

#Factorial
'''
n=int(input())
fact=1
for i in range(1,n+1):
    fact*=i
print(f"Factorial of {n} is: {fact}")
'''

#Fibonacci Series
'''
n=int(input())
a=0
b=1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b
'''

#Sum of Factorial of number
'''
n=int(input())  
sum=0
fact=1
for i in range(1,n+1):
    fact=fact*i
    sum+=fact
print(sum)      
'''    
    


    

