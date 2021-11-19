# <<<<<<<<<<<<<<<[ FOR LOOPS CONCEPT IN PYTHON]>>>>>>>>>>>>>>>>>>>>>>>>

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 

a="abcd"
for c in a:   # here c is a variable and takes each character of the string one by one and print it!!!!
    print(c)

 # note print have 2 parameter first what to print and second the end or seperate means if we want any spaces or not.!!!
# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 

# range in the python
# in case of range we have 3 things as mention below
#start means where to start , stop means where to stop and stride means how we reach from start to stop the condition for 
#the way of moving forward..!

#range( start,stop,stride)
# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 

n=int(input())
#for i in range(0,n,1): # here 1 means increment of 1...!
    
    # if we write like this the value will go upto n-1 means if  the value of n is 5 it will go till 4 and stops..!
    
for i in range(1,n+1,1):
# if we want to go to the exact value of n we entered then we have to replace n with n+1 in the above code....!!!!

  
    print(i)

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


n=int(input())
for i in range(n+1):  # here only value of range is given.!
                      # by default start is 0 
                      #by default stride/step is 1
    print(i)
# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 



n=int(input())
# for i in range(n+1,1):
#     print(i)
# the above pattern donot anything but simply print n.

for i in range(1,n+1): #it takes first argument for start
                       # second argument is n+1
                       # third agrument is by default 1( step/stride)
    print(i)
# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


# numbers for n to 1
n=int(input())
for i in range(n,0,-1):  # one number ahead of second argument print krega in case of decreasing sequence..!
    print(i)

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


### Print numbers starting from a and going till b and is multiple of 3

#a<b
a=int(input())
b=int(input())
for i in range(a,b+1,3):  # not good logic for  printing the multiple of 3.
    print(i)
# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


# first method to print multiple of 3
#a<b
a=int(input())
b=int(input())

for i in range(a,b+1,1):
    if i%3 == 0:
        print(i)
    
# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


# a<b
a=int(input())
b=int(input())
# first put condition for all the possible remainder ..! then ensure the loop start with the multiple of number you want to 
#start..!

if a%3==0:
    n=a
elif a%3==1:
    n=a+2
else:
    n=a+1
for i in range(n,b+1,3):
    print(i)

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


### check wether a number is prime or not.!

n=int(input())
flag=False
for d in range(2,n,1):
    if n%d==0:
        flag=True
if flag:
    print("not prime number")
else:
    print('prime number')

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


### (break keyword)

#### break is used when we want to exit from the loop!!

i=1
while i<10:
    if i==5:
        break
    print(i)
    i=i+1

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


n=int(input())
d=2
flag=False
while d<n:
    if(n%d==0):
        flag=True
        break
    d=d+1
if flag:
    print('not prime')
else:
    print('prime')

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


n=int(input())
flag=False
for d in range(2,n,1):
    if n%d==0:
        flag=True
        break
if flag:
    print("not prime number")
else:
    print('prime number')

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


n=int(input())
k=2

while k<=n:
    d=2
    flag=False
    while d<k:
        if k%d==0:
            flag=True
            break
        d=d+1
    if (not(flag)):
        print(k)
    k=k+1

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


### else keyword with loops

#### code inside else will not be executed if while/for loop is finished because of break statement ( very very important logic)!

i=1
while i<10:
    print(i)
    i=i+1
else:
    print('this will be printed once at the end')

for i in range(1,10):
    print(i)
else:
    print('this will also be printed once at the end')

for i in range(1,10):
    print(i)
print('this will also be printed once at the end')

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


# use of else in case of for loops here break is used so it not enter into the else part !!!!
for i in range(1,10):
    if i==5:
        break
    print(i)
else:
    print('this will also be printed once at the end')

 # - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


# prime numbers by using else statement in case of loops:---
n=int(input())
flag=False
for d in range(2,n,1):
    if n%d==0:
        flag=True
        break
else:
    print('prime number')

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


### continue keyword in python

#### it is used when we want to skip a iteration..! and as we use continue it wil go to the top of the loop again and pic the next number..!!

#### in case of for loop continue krne ke baad wo for mein pehle jaakr value value change krega then execute 

#### in case of while loop continue krne ke baad wo while mein direct execute krega with no value updated because in while loop value is not updated at the starting position it is updated at the ending position..!

# print all even numbers in a range except which are multiple of 7!

n=int(input())

for i in range(2,n+1,2):
    if i%7==0:
        continue
    print(i)

 # - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


# print all even number twice in a given range and multiple of 7 should be printed only once..!!
n=int(input())
for i in range(2,n+1,2):
    print(i)  # for  printing first time...!
    if i%7==0:
        continue
    print(i)   # for printing second time!!!

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


# print all even number twice in a given range and multiple of 7 should be printed only once..!!
n=int(input())
i=2
while i<=n:
    if i%7==0:
        i=i+2   # if we increment here it will work and it we incement as only in general way it will not work properly!
        continue
    print(i) 
    i=i+2

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


 ### Pass keyword in python:
 
 ##### in case of python if we write if keyword or while loop or for loop then we should have to write something inside it . its necessary just     opposite to java and c++ where it is not necessary..!
 
 #### if we have to achieve same we should here pass keyword..!
 
 #### it is very useful to structure the code..!


# in case of python if we write if keyword or while loop or for loop then we should have to write something inside it . its 
#necessary just opposite to java and c++ where it is not necessary..!

# if we have to achieve same we should here pass keyword..!

i=3
if i<7:
    pass
print("hey")
    
# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


i=1
while i<=3:
    pass
    i=i+1  # here writing updation condition is necessary( important)!!!
print("hey")

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 



for i in range(1,4):
    pass
print("end")