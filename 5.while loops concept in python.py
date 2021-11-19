# <<<<<<<<<<<<<[ CODING NINJAS PYTHON PROGRAMMING]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# <<<<<<<<<<<<<[Concept of while loops in python]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


### concept of while loops in python

# print 1  upto n times input by the users...!

n=int(input())
count=1
while count<=n:
    print(1)
    count=count+1
# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


# print first n natural numbers as per the input by the users.
n=int(input())
count=1
while count<=n:
    print(count)
    count=count+1
# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


### Primality check (check wether a number is prime or not)

n= int(input())
d=2
flag=False # flag is a marker whether the number divided by any of the number..!
while d<n:
    if(n%d==0):
        flag=True
    d=d+1
    
if flag==True:
    print("the number is not prime")
    
else:
    print("the number is prime")

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


### nested loops concept in python

# print all prime numbers between the given range of numbers .........!!!!
n= int(input())
k=2
while k<=n:
    d=2
    flag=False # flag is a marker whether the number divided by any of the number..!
    while d<k:
        if(k%d==0):
            flag=True
        d=d+1
    if not(flag):
        print(k)
    k=k+1

print(100,20)