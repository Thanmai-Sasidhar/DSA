#print numbers from 1 to 5
'''
i=1
while i<=5:
    print(i)
    i+=1
'''

#Count the no of digits
'''
count=0
n=12345
while n>0:
    n=n//10
    count+=1
print(count)    
'''

#Reversing the number(Digit)

#FORMULA : rev = rev * 10 + digit
'''
rev=0
n=12345
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print(rev)    
'''

#Reverse Number(String)
'''
n=int(input())
s=0
while n!=0:
    r=n%10
    s+=r
    n//=10
print(s)    
'''

#Even or Odd
'''
n=int(input())
for i in range(n+1):
    if i%2==0:
        print(i,end=" ")   
'''

#Digit Sum
'''
n=int(input('enter num='))
s=0
while n!=0:
    r=n%10
    s+=r
    n=n//10
print('sum:',s)
'''

#Natural numbers
'''
n=int(input())
i=1
while i<=n:
     print(i)
     i+=1
'''     




    
