# Static Data Structures 
'''
--> Arrays : It is a collection of elements, which stores in a contiguious memory location
 
    Index value of an array starts from 0
    
    Array access only similar data type like 
    1.array of integers : 1,2,3,4,5,6
    2.array of float : 1.2,2.3,4.5,6.7,7.8
    3.array of characters : a,b,c,d,e,f
    4.array of strings : apple,banana,kiwi...
    
    Characteristics of array :
    1.Fixed size
    2.same data type
    3.Accessed through index 
    4.contiguious memory
--> 
'''
#Accessing array elements through index 
'''
arr=[1,2,3,4,5,6,7,8,9]
print(arr[2])
print(arr[-2])

arr=list(map(int,input().split()))
print(arr[2])
print(arr[-2])
'''

#Traversing an array 
'''
arr=list(map(int,input().split()))
for i in range(len(arr)):
    print(arr[i],end=" ")
'''

#Minimum  element from an array

## The time complexity will be O(n) for both methods of for loop (or) sort because we iterate over n elements
'''
arr=list(map(int,input().split()))
min_val=arr[0]
for i in arr:
    if arr[i]<min_val:
        min_val=arr[i]
print("Minimum value of array is : ",min_val)
'''

#Maximum Element 
'''
arr=list(map(int,input().split()))
max_val=arr[0]
for i in arr:
    if arr[i]>min_val:
        max_val=arr[i]
print("Minimum value of array is : ",max_val)         
'''

#String 
'''
#Reverse a word in a String
s=input().split()
for i in s:
    print(i[::-1],end=" ")
'''

#Minimum value in string Lexiographically
'''
s=input("Enter the words : ").split()
min_val=s[0]
for i in s:
    if i<min_val:
        min_val=i
print("Smallest word : ",min_val)        
'''
'''
Eg:
b a d
b a d d
b a d d d
Here it will check the first letter of all words then if we have same letter then we will check the next letter
'''

#ceasar cipher(COMPANY SPECIFIC QUESTION)
'''
s=input("Enter the Word : ")
key=int(input())
result=""

for ch in s:
    if ch.isalpha():
        if ch.islower():
            new=chr(ord(ch)+key)
            result+=new
        else:
            new=chr(ord(ch)+key) 
            result+=new   
print(result)
'''

'''
Eg:
Input:   abcdef
         1
Output : bcdefg
'''
  
