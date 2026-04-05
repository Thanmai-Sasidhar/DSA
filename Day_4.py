#Time complexity

'''
n ->n//2 -> n//4-> n//8 -> n//16 -> n//32 -> n//64 -> n//128
O(log n)



def expo(a,b):
    if b==0:
        return 1
    elif b%2==0:
        return expo(a,b)
    else:
        return a*expo(a,b-1)
    #O(n2)
'''    
#Space Complexity
'''
arr=[] 
for i in range(n):
    arr.append(i)
'''
#Here the sapce complexity is O(n)
    
#Important Programs asked in interviews
'''
Armstrong Number
Strong Number
Nivins number
Happy number
Atomorphic number
Magic number
'''
#ARMSTRONG NUMBER
'''
num=int(input())
copy=num
sum=0
while num>0:
    r=num%10
    sum+=r**3
    num//=10
if copy==sum:
    print(sum,"is Armstrong Number")
else:
    print(copy,"Not an Armstrong Number")
'''

#Nivens
'''
num=int(input())
copy=num
sum=0
while num>0:
    r=num%10
    sum+=r
    num//=10
if copy%sum==0:
    print("Nivins Number")
else:
    print("Not a nivins number")  
'''

#Strong number
'''
num=int(input())
temp=num
sum_fact=0
while temp>0:
    digit=temp % 10   
    fact=1
    for i in range(1, digit + 1):
        fact*=i        
    sum_fact+=fact
    temp//=10

if sum_fact==num:
    print("Strong Number")
else:
    print("Not a Strong Number")
'''

#Strong Number using math
'''
import math as m

num=int(input())
sum=0
for i in str(num):
    sum+=m.factorial(int(i))
print(sum)
if sum==num:
    print("Strong Number")
else:
    print("Not a Strong Number")
'''    
