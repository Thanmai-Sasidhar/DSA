#Approaches

#Naive Approach 
#Brute Force 
#Greedy Approach
#math Approach

#PRIME NUMBER

#Cons --> #Executes slowly for Big number (in Nano seconds)
#         #Unnecessary Repetations

#BRUTE FORCE  
'''
n=int(input())
for i in range(2,n):
    if n%i==0:
        is_prime=False
        break
if is_prime:
    print(f"{n} is Prime Number")
else:
    print(f"{n} is Not a Prime Number")    
'''

#MATH APPROACH
'''
num=int(input())
is_prime=True
i=2
while i*i<=num:
    if num%i==0:
        is_prime=False
        break
    i+=1
if is_prime:
    print(f"{num} is a Prime Number")
else:
    print(f"{num} is Not a prime")        
'''


    
        

