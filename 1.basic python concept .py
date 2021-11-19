
      # <<<<<<<<<<<<<<<<<[ BASIC OF PYTHON PROGRAMMING]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


### Print helloworld

print("hello")
print('hello')
#agar hum lagatar print function python mein likhege to wo message ko enter ke saath print krega by default..means wo saare 
#print message ko alag alag lines mein print krega by default....!!!
print("hello")
#last line is the output of the particular shell..!!


# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 

### Variables

a=10  #create storage for u and u can access that storage name "a" contain the data
b=20

sum=a+b
abc=10
print(sum)
print(abc)
print("sum")

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


### Variable Naming

abc1=10
ab_c1=10
_ab=10
# (12ab=12) you cannot start with the digit while defining variables.

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 



### Assign different types of data to a variable

a=10
a=20
a='sudeep kumar'
a

# in case of python if we write (a=10,a="abc"...etc) it means python stores 10 in 
#the memory anywhere and a has the address of that storge or u can say a is 
#pointing towards that address of 10 and if we change the value of "a" to anything
#suppose a string "sudeep" means now python will again store "sudeep" in different
#location and now "a" will point to the string "sudeep" instead of "10",instead of
#replacing the value of "a". 

#hence it is different from other language like c++ or java they make a storage
#for "a" of a specific types(like int ,float,double,char,string.etc) means you 
#cannot store that data in "a" for which the data type is not defined.. which
# is not the problem in case of python language..!!!!!

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


a="abc"
print(type(a))  # (type) is a command which will tell what kind of data
                # the variable stored....!!!!!!

a=10
print(type(a))

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


### Python Numbers

a1=23
a2=3.4
a3=4+5j   # complex number (a+bj)
print(a1)
print(a2)
print(a3)
print(type(a1))
print(type(a2))
print(type(a3))




# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


a=10
print(id(a)) # (id) command tell the unique identification of the variable storage
a=a+1
print(id(a))
a     #last line is the output of the programe so output is 11.


#yha pr pehle compiler a+1 compute krega aur usko alag address pr store krega
#aur ab "a" us new address ko point krega aur output 11 dega....!!




# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 

a=10
b=10

print(id(a))
print(id(b))
#both id will be same means a and b point to the same address which conatains 10
#(if both variable have the same value )

#note:-( if 2 variables have the same value in the range (-5 to 256 ) then their)
#      (id or addresses are same , only for the above specified range )
#      (BUT NUMBER OUTSIDE THAT GIVEN RANGE WILL NOT FOLLOW THE ABOVE RULE).

a=10
id1=id(a)
b=a+2-2
id2=id(b)
print(id1)
print(id2)

#note by any arithmatic operation if we make value of 2 variable same then
# the id must be same for ex:::----

# here we make b=a by using (b=a+2-2) hence the id are same for both the cases.

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


### Range of Integers in Python

# Range of intergers is not a big problem in python because python can store any range of integers either it is very big,
# very small any thing if u give  that much memory to the python means if memory is sufficient range of integers is anything 
# in the python programming...!!!!

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


### Arithmetic Operators in Python

# (+, ,-, *, /, //, **, %)
a=10
b=4
print(a+b)
print(a-b)
print(a*b)
print(a/b) # it will give you the exact value with decimal which is not as generally found in c++ or java.!
print(a//b) #( "//" double slash is used to do integer division)
print(a**3) #( "**" exponentiation means value to the power something u write with "**" like (10**3) means 10 to the power 3!
print(a%b)   #( "%" modulous operator)

# (+, ,-, *, /, //, **, %)

# very very important code:
a=-10
b=4
print(a+b)
print(a-b)
print(a*b)
print(a/b) # it will give you the exact value with decimal which is not as generally found in c++ or java.!
print(a//b) #( "//" double slash is used to do integer division)
print(a**3) #( "**" exponentiation means value to the power something u write with "**" like (10**3) means 10 to the power 3!
print(a%b)   #( "%" modulous operator)

2+(3*4) # 14 0r 20

2*3/4  # doenot matter what operation is done first.

(2*3)//4 # first do multiplication then integer divison

# simple interest to lower integer
p=100
r=12
t=2
si= (p*r*t)//100
print(si)


# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


# Farenheit to celcius conversion
f=100
c=(f-32) * 5/9
print(c)
c=(f-32) * 5//9
print(c)

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 



### Taking inputs from the user in Python

a=input()   # taking input from the user..!
           # by default input() command treat all input as stirng..!
a


a=input()
print(type(a))

b=input()
print(type(b))
m=a+b
print(m) # it will not give addition because by default input in python is treated as string input...!!!!!!!!!
         # so it will concatenate the 2 values giving the output below..!!!!!!!!!!!

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


   ### Conversion of data types in Python

b='34'
print(type(b))
c=int(b)
print(type(c))
d=int(3.7)  # convert floating points no to integer note there is no round off..!
print(d)
# e='12df4'
# print(int(e))  ##give u the error because int should be off base 1o numbers



a=int(input())
b=int(input())
c=a+b
print(c)  #now it is treated as integer inputs............!!!!!!!
d=float(input())
e=float(input())
f=d+e
print(f)   # now it is treated as float inputs.....!!!!!!!!!

# note:
          
# to print the float number upto 2 decimal points
 # formatted_float = "{:.2f}".format(a_float)