# <<<<<<<<<<<<<<[ PASSING VARIABLES THROUGH FUNCTIONS IN PYTHON PROGRAMMING ]>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# def increment(a):
#     a=a+2
#     return a

# a=2
# b=increment(a)
# print(a)            # note:------------in this case the output is 2 for a.
# print(b)            # now the value returned by function stored in b so it prints the vlaue 4.



# <<<<<<<<<<<[ Passing lists to a functions in python]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def increment(li1):
    # li1[0]=li1[0]+2
    li1=[3,3,4]       #here we change the refrence!!!!
    return li1


li=[1,2,3,4]
li2=increment(li)
print(li)            # in this case the funtion returns and the value of li[0] is changed directly....!!!!!!!!
                     # because lists are mutable means li and li1 has the same reference and any changes made in the any one of
                    # them will reflect on the other list.............!!!

print(li2)
