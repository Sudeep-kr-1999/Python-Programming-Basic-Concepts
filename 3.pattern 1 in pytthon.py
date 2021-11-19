# <<<<<<<<<<<<<<<<<<<<[ pattern 1 in python programming]>>>>>>>>>>>>>>>>>>>>>>>>>>
# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 

### Pattern in the loops in python

# ****
# ****
# ****
# ****


n=int(input())
i=1
while(i<=n):
    j=1
    while(j<=n):
        print("*",end="") # end with empty string nothing will be printed nor will it take enter by default means we are
                          # in the same line.!
        j=j+1
    print() # don't print anything but it still print a new line by default!
    i=i+1

        
    
# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 

### Square Pattern in python

# 1111
# 2222
# 3333
# 4444

# n=int(input())
# i=1
# while(i<=n):
#     j=1
#     while(j<=n):
#         print(i,end="") # end with empty string nothing will be printed nor will it take enter by default means we are
#                           # in the same line.!
#         j=j+1
#     print() # don't print anything but it still print a new line by default!
#     i=i+1

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 

# 1234
# 1234
# 1234
# 1234


# n=int(input())
# i=1
# while(i<=n):
#     j=1
#     while(j<=n):
#         print(j,end="") # end with empty string nothing will be printed nor will it take enter by default means we are
#                           # in the same line.!
#         j=j+1
#     print() # don't print anything but it still print a new line by default!
#     i=i+1

 # - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


4321
4321
4321
4321


# n=int(input())
# i=1
# while(i<=n):
#     j=1
#     while(j<=n):
#         print(n-(j-1),end="") # end with empty string nothing will be printed nor will it take enter by default means we are
#                           # in the same line.!
#         j=j+1
#     print() # don't print anything but it still print a new line by default!
#     i=i+1


# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


### Triangular Pattern in python

# 1
# 12
# 123
# 1234


# n=int(input())
# i=1
# while(i<=n):
#     j=1
#     while(j<=i):
#         print(j,end="") # end with empty string nothing will be printed nor will it take enter by default means we are
#                           # in the same line.!
#         j=j+1
#     print() # don't print anything but it still print a new line by default!
#     i=i+1

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


# 1
# 23
# 345
# 4567


# n=int(input())
# i=1
# while(i<=n):
#     j=1
#     p=i
#     while(j<=i):
#         print(p,end="") # end with empty string nothing will be printed nor will it take enter by default means we are
#                          # in the same line.!
#         j=j+1
#         p=p+1
#     print() # don't print anything but it still print a new line by default!
#     i=i+1

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


# 1
# 2 3
# 4 5 6
# 7 8 9 10


n=int(input())
i=1
p=1
while(i<=n):
    j=1
    while(j<=i):
        print(p,end="") # end with empty string nothing will be printed nor will it take enter by default means we are
                         # in the same line.!
        j=j+1
        p=p+1
    print() # don't print anything but it still print a new line by default!
    i=i+1

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


## Character Pattern

## PRINT Kth Alphabet

# print kth alphabet
# very very important logic in the programming..!!!!!!!!
k=int(input())
# 'A'+k-1
 #ord('B') ord() give the corresponding ascii value of character
 #chr(66) chr() give the corresponding character related to ascii value

x=ord('A')
asciiTarget=x+k-1
targetChar=chr(asciiTarget)
targetChar


# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


# ABCD
# ABCD
# ABCD
# ABCD


# n=int(input())
# i=1
# while(i<=n):
#     j=1
#     while(j<=n):
#         #print jth alphabet
#         charP=chr(ord('A')+j-1)   # VERY VERY IMPORTANT LOGIC
#         print(charP,end="") # end with empty string nothing will be printed nor will it take enter by default means we are
#                           # in the same line.!
#         j=j+1
#     print() # don't print anything but it still print a new line by default!
#     i=i+1

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


# ABCD
# BCDE
# CDEF
# DEFG


# n=int(input())
# i=1
# while(i<=n):
    
#     j=1
#     start_char=chr(ord('A')+i-1)  #important step
#     while(j<=n):
#         #print jth alphabet
#         charP=chr(ord(start_char)+j-1)   # VERY VERY IMPORTANT LOGIC
#         print(charP,end="") # end with empty string nothing will be printed nor will it take enter by default means we are
#                           # in the same line.!
#         j=j+1
#     print() # don't print anything but it still print a new line by default!
#     i=i+1