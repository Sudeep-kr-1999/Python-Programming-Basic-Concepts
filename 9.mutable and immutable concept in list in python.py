#<<<<<<<<<<<<<<<<<<<<<<<<<[MUTABLE AND IMMUTABLE CONCEPT IN LIST IN PYTHON ]>>>>>>>>>>>>>>>>>>>>>

# NOTE:----------> Variables are immutable in python............!!!!!!!!!!!!!!!!!
# Concept in which you cannot change into the memory you can change only the refrences this concept is called immutable....!!
# ( the above concept is the immutable concept in case of variables)


# <<<<<<<<<< [ MUTABLE CONCEPTS IN CASE OF LISTS]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# DEFINITION:--- IF 2 list are pointing to same reference and if you make any changes in one list the same change will reflect on
#                the other list.....................!!!!!!!!!!!!!



# example code:----- (immutable in case of variables)

# x=3
# a=3
# # here "x" and "a" are having same value so they are pointing to the same reference so their id will be same!!!
# print(x)
# print(a)
# print(id(x))
# print(id(a))
# a=4              #  here we change the value of a=4 so now "x" and "a" are now pointing to different numbers so different
#                  #  references so id of "a" and "x" will be different now.............!!!!!!!!!!
# print(a)
# print(id(a))




# example code :----------( mutable in case of lists)

li=[1,2,3,4]           # li is a initial list
print(li)
li2=li                 # here li2 as same list as li
print(li2)
li2[1]=4            # here we change the value of index 1 in th li2 list, but since the li and li2 are pointing to the same
                   # reference as per the statement( li2=li) so any changes made on li2 will also reflect in li
                   # so there will be a change in both li and li2 index 1 element and it will become 4 in this case.....!!!!!
print(li)
print(li2)

li2=[3,3,4]   # now in this step li 2 now pointing to the different refrernce so now both the list are independent to each other
             # means these are mutable now !!!!!!!!!!!!

print(li)
print(li2)