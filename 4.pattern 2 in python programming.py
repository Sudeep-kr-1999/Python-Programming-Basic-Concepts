# <<<<<<<<<<<<<<<<<<<<<[ pattern 2 in python programming]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 
# ****
# ***
# **
# *


n=int(input())
i=1
while(i<=n):
    j=1
    while(j<=n-i+1):
        print("*",end="")
        j=j+1
    print()
    i=i+1
        
# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


# reverse triangle

#    *
#   **
#  ***
# **** 
# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


n=int(input())
i=1
while i<=n:
    spaces=1
    while spaces<=n-i:  # while loop for spaces
        print(" ",end="")
        spaces=spaces+1
    star=1
    while star<=i:   # while loop for stars
        print("*",end="")
        star=star+1
    print()
    i=i+1
    
# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


#    1
#   12
#  123
# 1234 
   


n=int(input())
i=1
while i<=n:
    spaces=1
    while spaces<=n-i:
        print(" ",end="")
        spaces=spaces+1
    p=1
    j=1
    while(j<=i):
        print(p,end="")
        j=j+1
        p=p+1
    print()
    i=i+1

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 



#  isosceles pattern
#    1
#   121
#  12321
# 1234321 

n=int(input())
i=1
while i<=n:
    spaces=1
    
    #spaces
    while spaces<=n-i:
        print(" ",end="")
        spaces=spaces+1
    p=1
    j=1
    
    #increasing sequence
    while(j<=i):
        print(p,end="")
        j=j+1
        p=p+1
        
        #decreasing sequence
    p=i-1
    while p>=1:
        print(p,end="")
        p=p-1
    print()
    i=i+1

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 

#     5
#    45
#   345
#  2345
# 12345

n=int(input())
i=1
while(i<=n):
    j=1
    p=1
    while(j<=n):
        if j>=(n+1-i):
            print(p,end="")
        else:
            print(" ",end="")
        j=j+1
        p=p+1
    print()
    i=i+1