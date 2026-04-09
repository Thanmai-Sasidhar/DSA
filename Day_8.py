#searching in array data structures:
#searching on number/string
#OCCURENCES
#finding the duplicate elements-print duplicate,remove duplicate
#1 2 3 4 5 6
#linear ->approach
#arr= [10,20,30,40,50]
#search =30
#30 is found at index value 2
'''arr=list(map(int,input("enter an element with spces").split()))
search=int(input("enter the element to be searched:"))
found= False
for i in range(len(arr)):
    if arr[i]== search:
        print("elements found at index:", i)
        found = True
        break
if not found:
    print("Elements not found!!!!!")'''

#dry run:
# arr=[1,2,3,4,5,6,7,7,7]
#search = 7
#for 0-> 8:
#if 0==7 1==7 2==7 3==7 4==7 5==7 6==7 7==7:
#break
#if not found:
#print(elements not found)

#for string
'''arr=input("enter elements with spaces:").split()
search=(input("enter the element to be searched:"))
found= False
for i in range(len(arr)):
    if arr[i]== search:
        print("elements found at index:", i)
        found = True
        break
if not found:
    print("Elements not found!!!!!")'''

arr=list(map(int,input("enter an element with spces").split()))
search=int(input("enter the element to be searched:"))
found= False
for i in range(len(arr)):
    if arr[i]> search:
        print("elements found at index:", i)
        found = True
        break
if not found:
    print("Elements not found!!!!!")


