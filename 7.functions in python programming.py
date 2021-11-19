# # <<<<<<<<<<<<<<<<<[ FUNCTION IN PYTHON PROGRAMMING]>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -
# # Functions in python programming!!

# #### Avoid repetition
# #### improve readibility
# #### for testing purpose


# n=int(input())
# r=int(input())

# n_fact=1
# for i in range(1,n+1):
#     n_fact=n_fact*i

# r_fact=1
# for i in range(1,r+1):
#     r_fact=r_fact*i

# n_r_fact=1
# for i in range(1,n-r+1):
#     n_r_fact=n_r_fact*i

# ans=n_fact//(r_fact * n_r_fact)
# print(ans)


# # - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -


# # syntax to write a function

# def fact(n):  # definition of a function and n is the number of input..!
#     n_fact=1
#     for i in range(1,n+1):
#         n_fact=n_fact*i
#     return n_fact

# a=int(input())
# b=fact(a)
# print(b)

# # - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -


# n=int(input())
# r=int(input())
# n_fact=fact(n)
# r_fact=fact(r)
# n_r_fact=fact(n-r)

# ans=n_fact//(r_fact * n_r_fact)
# print(ans)

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -

# check wether the number is prime or not................................!!!!!!!!!!!!!!!!!

# def isprime(n):
#     for d in range(2,n):
#         if (n % d==0):
#             break
#     else:
#         return True

#     return False


# print("enter the number you want to check=",end="")
# n=int(input())
# a=isprime(n)
# print(a)

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -
# print all prime numbers under the given range inserted by the user....!!!!!!!!!!!!!!!!!!!!1
# def isprime(n):
#     for d in range(2,n):
#         if(n%d==0):
#             break
#     else:
#         return True

#     return False

# def printprime(x):
#     for k in range(2,x+1):
#         is_prime=isprime(k)
#         if(is_prime):
#             print(k)

# print("enter the number upto which you want to search the prime numbers:",end="")
# n=int(input())
# call=n    # we cannot call function directly by writing printprime(n) it will not occur because we cannnot call an int value
#           # directly so we have to make one more variable which stores the value of n and use it to call the function in this case
#           # the variable is call variable.................!!!!!!!!!
# printprime(call)


# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -
# calculate ncr for the given valueso fo r and n.!!!!!!!!!!!!


# def fact(n):
#     n_fact=1
#     for i in range(1,n+1):
#         n_fact=n_fact*i
#     return n_fact

# def ncr(n,r):
#     n_fact=fact(n)
#     r_fact=fact(r)
#     n_r_fact=fact(n-r)
#     ans=n_fact//(r_fact * n_r_fact)
#     return ans

# print("enter the value of n:",end="")
# n=int(input())
# print("enter the value of r:",end="")
# r=int(input())
# print("ncr value is:",end="")
# ncr=ncr(n,r)
# print(ncr)


# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -
# function calling actually work in the principle of first in  and last out principle(FILO OR LIFO) principle
# stack is generally a  thing which follow the principle of first in and last out(LIFO OR FILO )

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<,[ SCOPE OF THE VARIABLE  CONCEPT]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 2 kind of scope
# 1. local variable:- define inside a function
# 2. global variable:- define outside any function

# a1=10    #a1 is a global variable the global variable can be call anywhere either it is defined earlier or later we can use it in
#          # stage...............!!!!!!!!!!

#          # but we should take care  that we should definitely define the variable before the function call ....otherwise it will
#          # not work properly................!
# def f1():
#     b1=12  #b1 is a local variable
#     print(b1)
#     print(a1) # can print a global variable inside the functions
# f1()             #even after calling the functions we cannot print the value of b1 outside the function scope.. !!!!!!
#                  # it will be printed inside the function scope....!!!!!!!!!!
# print(a1)
# print(b1) it will not work because b1 is not defined...!!!!!!!

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -

# a4=13
# def f4():
#     a4=12       # if we change the value python assumes that you want to create a local variable( very very important).......!!!
#     print(a4)        # this print 12
#     print(id(a4))
# print(a4)            # this print 13
# f4()
# print(a4)        # this print 13
# print(id(a4))


# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -

a4=13
def f4():
    global a4  # if we change the value python assumes that you want to create a local variable( very very important).......!!!
              # but if we specify it as global explicitly then it act as global and used outside the scope of function....!
    a4=12
    print(a4)        # this print 12
    print(id(a4))
print(a4)            # this print 13
f4()
print(a4)        # this print 12
print(id(a4))


# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -

                 # <<<<<<<<<<<<<<<[ Default arguments in functions in python]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# note:- we cannot either more or either less than the number of argument to a function that we decide while defining the function.!

# # for ex:
# def f(n):
#     print(n)

# # f(3,3)   here for the function defined only one argument is necessary but 2 were given so it will not work
# # f()      here also for the function defined atleast one argument is necessary and no argument is given so it will not work...!
# f(3)       # it will work because appropriate number of parameters is given........!!

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -

# def sum(a,b):
#     return a+b

# def sum(a,b,c):
#     return a+b+c

# <<<<<<<<<<<<<<<[ better way to do above coding for sum as it take different functions for different number of arguments]>>>>>>!
               # <<<<<<<<<<<<<<<[ Default arguments in functions in python]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# note:------- default argument should be given from the right side of the function parameter means all non default arguments
               # should be before the default arguments provided to the function.......!!!!!!!!!!!!!!!

# def sum(a,b,c=0):
#     return a+b+c

# print(sum(2,3,4))
# print(sum(2,3))

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -

def f1(a,b,c=2,d=0):
    return a+b+c+d
print(f1(2,3,4,5))
print(f1(2,3))
print(f1(2,3,5))
print(f1(2,3,d=5)) #  note:------> in this case after assigning 2 values to the non default argument the next value will not go
                  #  directly to "c" instead it will go to "d" because here we specify that we are assigning the third value to
                  #  "d"  explicitly..( note this is only possible only when you are done with non default arguments )!!

# note:----------> values assigning process will always start from the left end parameter of the function and goes on.......!!