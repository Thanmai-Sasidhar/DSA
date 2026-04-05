#Pattern 1(SQUARE)
'''
n=int(input())
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()    
'''

#Pattern 2 (Hollow Square)
'''
n=5 
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")    
    print() 
'''

#Pattern 3(DIAGONAL HOLLOW SQUARE) 
''' 
n=5 
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or i==j or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")    
    print()
'''    
#Pattern 4(HOUR GLASS)  
'''
n=5 
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i==j or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")    
    print()
'''    
#Pattern 5 (BUTTERFLY)
'''    
n=5 
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==j or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")    
    print()       
'''

#Pattern 6(COORDINATE AXIS *)
'''
n=5
for i in range(n):
    for j in range(n):
        if i==n//2 or j==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()                 
'''

#Pattern 7(RIGHT ANGLE TRIANGLE)
'''
n=5
for i in range(n):
    for j in range(n):
        if i==n-1 or j==0 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()            
'''
#Pattern 7(MIRRORED RIGHT ANGLE TRIANGLE)
'''
n=5
for i in range(n):
    for j in range(n):
        if i==n-1 or j==n-1 or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()            
'''
#Pattern 8(INVERTED RIGHT ANGLE TRIANGLE)
'''
n=5
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()        
'''

#Pattern 9(MIRRORED INVERTED RIGHT ANGLE TRIANGLE)
'''
n=5
for i in range(n):
    for j in range(n):
        if i==0 or j==n-1 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print() 
'''
    
#Pattern 10  (FULL RIGHT ANGLE TRAINGLE)
'''
n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()                
'''

#Pattern 11
'''
    *
   ***
  *****
 *******
*********
''' 
''' 
n=5
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(2*i-1):
        print("*",end="")
    print()       
'''

#Pattern 12
'''
*********
 *******
  *****
   ***
    *
'''
'''
n=5
for i in range(n):
    print(" "*i,end="")
    for j in range(2*(n-i)-1):
        print("*",end="")
    print()  
'''

#Pattern 13
'''
    *
   * *   
  * * *    
 * * * *     
* * * * *      
'''  
'''
n=5
for i in range(n):
    print(" "*(n-i-1),end="")
    for j in range(i+1):
        print("*",end=" ")
    print()    
'''

#Pattern 14
'''
* * * * * 
 * * * * 
  * * *  
   * * 
    * 
'''
'''
n=5
for i in range(n):
    print(" "*i,end="")
    for j in range(n-i):
        print("*",end=" ")
    print()    
''' 

#Pattern 15

'''
* * * * * 
*       * 
* * * * * 
* 
* 
'''

n=5
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n//2 or (i<3 and j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()                                    
