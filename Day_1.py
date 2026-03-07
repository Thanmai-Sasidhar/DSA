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

#Reversing the number

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
