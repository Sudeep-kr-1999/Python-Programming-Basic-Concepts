
# <<<<<<<<<<<<<[ CODING NINJAS PYTHON PROGRAMMING]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 

### Booleaan Datatypes



a=True #  True and false must be start with "T" and "F". these are reserved keyword.
b=False # True and False donot need to be put in single quotes or double quotes...!
c="ninjas"
type(a)  # a is boolean...!!
# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


### Relational Operators

a=10
b=20
print(a>b)  # give output false..!
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)
# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 



### Logical Operators in Python

c1=a>10
c2=b>10
print(c1)
print(c2)

r1=c1 and c2 # "and" means both have to be true.!!!!!!!!!!!
print(r1)
r2=c1 or c2  # "or" means at least one should be true!!!
print(r2)
r3=not(c1) # this means c1 is false and  so not of c1 is true..!!!!!!!!!!
# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


### If-Else In Python Programming

a=True
if a:
    print("i am inside if")  # "indentation" is very very important.
    print("hello sudeep welcome")
else:
    print("i am inside else")

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


# Check number to be "odd" or "even"!!!!!!!
n=int(input())
r=n%2
is_even=(r==0)

if is_even:
    print("n is an even number")
else:
    print("n is  an odd number")


    # - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


# Check number to be "odd" or "even"!!!!!!!
n=int(input())

is_even=(n%2==0)

if is_even:
    print("n is an even number")
else:
    print("n is  an odd number")
    

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Check number to be "odd" or "even"!!!!!!!
n=int(input())

if n%2==0:
    print("n is an even number")
else:
    print("n is  an odd number")
    
    
# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


##### Check number to be "odd" or "even"!!!!!!!
n=int(input())

if n%2==0:
    print("n is an even number")
    
    #if else is not included it only show the input nothing else..!!!!!

x=5
if x<6:
    print("hello")
if x==5:
    print("hi")
else:
    print("hey")
 # - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


### Using Operations in if -else 

a=int(input())
b=int(input())

c1=a>10
c2=b>10

r=c1 and c2
if r:
    print("both > 10")
else:
    print("no they are not")



a=int(input())
b=int(input())

if a>10 and b>10:
    print("both > 10")
else:
    print("no they are not")

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 



n=int(input())
if n==7:
    print("it is 7")
else:
    print("no its not 7")
 # - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


### ELIF in Python ( just like else if)

#given three number a,b,c print largest numbers.

a=int(input())
b=int(input())
c=int(input())

if a>=b and a>=c:
    print(a)
    
elif b>=a and b>=c:
    print(b)

else:
    print(c)


n=int(input())

if n>10:
    print("red")
    
elif n>=5:
    print("green")
    
elif n>0:
    print("yellow")
    
    
# all the cases are mutually exclusive cases...!!!!!!!
# note: this code will work properly because this is right code and one  
#       thing to note here is order of the condition matter a lot in elif(if else condition)

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


n=int(input())

if n>=5:
    print("green")
    
elif n>10:
    print("red")
    
elif n>0:
    print("yellow")
    
# note: this code will not work properly because this is wrong code and one  
#       thing to note here is order of the condition matter a lot in elif(if else condition)    
# all the cases are mutually exclusive cases...!!!!!!!

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


### Nested IF-else in Python

# Check number to be "odd" or "even"!!!!!!!

n=int(input())

if n%2==0:
    print("n is an even number")
    if n==0:
        print("n is equal to zero")
else:
    print("n is  an odd number")
    
# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


m=int(input())
n=int(input())

if n%2==0:
        if m%2==0:
            print(1)
        else:
            print(2)
        
else:
    print(3)
        
# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 



start=int(input())
end=int(input())
w=int(input())

s=start
while (s<=end):
    celcius=int((s-32)*5/9)    # we use int to make float value to the integer value and simply print it..!
    
    print(s,"\t",celcius)
    
    s=s+w
