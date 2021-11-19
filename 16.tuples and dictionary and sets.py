                  #<<<<<<<<<<<<<<<<<<[ TUPLES CONCEPT IN THE PYTHON]>>>>>>>>>>>>>>>>>>>>>

# 1.TUPLES ARE VERY VERY SIMILAR TO LISTS........!!
# 2.Tuples are used when we want to put multiple elements together in the one variable.


# <<<<<<<<<<<<<<<<<<[ way to creating a tuple]>>>>>>>>>>>>
# a=[1,2] # it is the way of creating a list.

# b=(1,2) # it is a way of creating a tuple....!
# b=(1,)  # this is also a tuple

# note:----> actually in python by default multiple things tend to be a tuples!

# print(b)
# print(type(b))

#- -  - - - - - - - - - -  - - - - - - - - - - -- - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


# b,c=3,4
# e=5,6           # python assume "e" as a tuple..!
# print(b)
# print(c)
# print(e)
# print(type(b))
# print(type(c))
# print(type(e))

# # process of accessing elements in tuple is as same as in the lists by using indexes....!!!
# print(e[0])
# print(e[1])
# print(e[-1])
# print(e[-2])



# note:--- slicing in tuple is as same as it is used to be in the list...!!

# f=(1,2,3,4,5,6)
# print(f[0:3])
# print(f[3:])
# del f       # it will delete the tuple itself...!!!!

# difference between tuples and the list.................!!!
# 1. Tuples are immutable but lists are mutable......!!!!



#- -  - - - - - - - - - -  - - - - - - - - - - -- - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#- -  - - - - - - - - - -  - - - - - - - - - - -- - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#                  <<<<<<<<<<<<<<<<<<<<<<<<<<<<[TUPLE FUNCTIONS]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# a=(1,2,3)
# b=2,5

# for loops works as it is in tuple
# for i in a:
#     print(i)


# # checking availability of number in any tuple!!!!!!!!!
# print(1 in a)
# print(1 in b)


# # length operator
# print(len(a))
# print(len(b))


# # concatination of tuples....!!!
# print(a+b)

# # 2 dimensional tuples
# d=(a,b)        # it is a tuple of tuples ...........!!!!!
# print(d)

# # repitition of tuples
# e=a*4
# print(e)


# finding maximum
# print(max(a))
# print(max(b))

#comparison functions
# a2=(1,2,"a",(1,2))
# # print(min(a2))    # this will give error it cannot compare tuple, string and integer...>!


# a3=(2,2.2)
# print(min(a3))


# converting list to a tuple..........!
# li=[1,2,3,4]
# print(tuple(li))


#- -  - - - - - - - - - -  - - - - - - - - - - -- - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#- -  - - - - - - - - - -  - - - - - - - - - - -- - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# <<<<<<<<<<<<<<<<<<<<<<<<<[ VARIABLE LENGTH INPUTS AND OUTPUTS IN TUPLES]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# sum function in general way.........!!!
# def sum(a,b):
#     return a+b

# print(sum(1,2))


# sum function with the help of tuples............!

# def sum2(a,b,*more):
#     # print(a)
#     # print(b)
#     # print(more)    # it will print empty tuple.............!!
#     # print(type(more))
#     ans=a+b
#     for i in more:
#         ans=ans+i
#     return ans

# # input=sum2(2,3)
# answer=sum2(2,3,4,5)
# print(answer)



# def sum_diff(a,b):
#     return a+b,a-b

# c=sum_diff(4,1)
# print(c)     # it is a tuple.......!!




# def sum_diff(a,b):
#     return a+b,a-b,a*b

# c,d,f=sum_diff(4,1)
# print(c)
# print(d)
# print(f)

# e=sum_diff(4,1)
# print(e)

# note:-- we can get the output in both ways either in tuple or individual outputs...!!!

# note:====== no of values returning from the function should be same as the number of output required by the users.!!!





#- -  - - - - - - - - - -  - - - - - - - - - - -- - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#- -  - - - - - - - - - -  - - - - - - - - - - -- - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#- -  - - - - - - - - - -  - - - - - - - - - - -- - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#- -  - - - - - - - - - -  - - - - - - - - - - -- - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<[ INTRODUCTION TO DICTIONARIES]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#   note:---------> dictionary wil be created using curley braces...........!!!!
                    # dictionaries are mutable.....!!
# a={"the":1,"a":5,1000:"abc"}
# print(type(a))
# print(len(a))
# print(a)


# # syntax:------
# # a={"key1":"value1","key2":"value2","key3":"value3",............,"keyn":"valuen"}
# # note:-----> the key and value can be anything we want...........!!!!!


# # few more ways to create a dictionary
# b=a.copy()
# print(b)


# c=dict([("dict",3),("a",10),(2,3)])
# print(c)


# d=dict.fromkeys(["abc",32,4],10)  #here inside the big brackets is the keys and outside the big bracket is the value....!
# print(d)

# note:------- dict contain list and list contains pairs and each pair having first element as key and second element as value!!!




#- -  - - - - - - - - - -  - - - - - - - - - - -- - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#- -  - - - - - - - - - -  - - - - - - - - - - -- - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

#               <<<<<<<<<<<<<<<<<<<[ ACCESSING AND LOOPING IN THE DICTIONARIES]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# a={1:2,3:4.,"list":[1,23],"dict":{1:2}}

# print(a[0])   # it will not work because in dictionary we access the data by using the actual key of the dictionaries.!
# print(a[1])
# print(a[3])
# print(a["list"])
# print(a["dict"])

# print(a.get(1))
# print(a.get("list"))
# print(a.get("li"))         # it didnot give you error it give you output as "none"......!!!!!!!!
# print(a.get("li",0))     # here in this case get will not return "none" but it will return the value associated with the key if
#                         # key is present otherwise  the second argument is returned.........!!!!

# print(a.keys())
# print(a.items())        # it return the list of keys and values pairs..........!!!
# print(a.values())


# for i in a:
#     print (i)   # by default it give the keys of dictionaries
#     print(i,a[i])

# for i in a.values():
#     print(i)


# check if a key exist in the dictionary or not..!
# print("list" in a)    # check wether list key is present in the dictionary or not......!
# print("li" in a)
# print(2 in a)   # it will give false because 2 is not the key it is the value and the operation there check the key ..>!



#- -  - - - - - - - - - -  - - - - - - - - - - -- - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#- -  - - - - - - - - - -  - - - - - - - - - - -- - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<[ ADDING AND REMOVING DATA IN THE DICTIONARY]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# a={1:2,3:4.,"list":[1,23],"dict":{1:2}}
# a["tuple"]=(1,2,3)
# a[1]=10
# print(a)

# # update data!
# b={3:5,"the":4,2:100}
# a.update(b)    # this means "a" will be updated as per the dictionary "b" and if any thing new is available in "b"
#                # then it will added to "a"......!!!!!!!!
# print(a)


# #remove data
# a.pop("list")    # pop will take the key as the argument and it will delete that key as well as its value from the dictionary...!
# print(a)


# del a[1]
# print(a)

# a.clear()   # clear will remove everything from the dictionary but not the dictionary itself the dictionary is still there.....!!
# print(a)

# del a # it will delete the complete dictionary ...........!!!!!!!!!!!!


#- -  - - - - - - - - - -  - - - - - - - - - - -- - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#- -  - - - - - - - - - -  - - - - - - - - - - -- - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<[ PRINT ALL WORDS WITH FREQUENCY K]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# a="this is a word string having many many word"
# k=2
# words=a.split(" ")
# print(words)

# d={}
# # very very important logic
# for w in words:
#     if w in d:
#         d[w]=d[w]+1
#     else:
#         d[w]=1
# print(d)

# for w in words:
#     d[w]=d.get(w,0)+1

# print(d)
# for w in d:
#     if d[w]==k:
#         print(w)




# function for doing the work mention above.!

# def printkfrewords(str,k):
#        words=str.split()
#        d={}
#        for w in words:
#            d[w]=d.get(w,0)+1
#        for w in d:
#             if d[w]==k:
#                 print(w)

# a="this is a word string having many many word"
# k=2

# (printkfrewords(a,1))




#- -  - - - - - - - - - -  - - - - - - - - - - -- - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#- -  - - - - - - - - - -  - - - - - - - - - - -- - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#- -  - - - - - - - - - -  - - - - - - - - - - -- - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#- -  - - - - - - - - - -  - - - - - - - - - - -- - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

#                     <<<<<<<<<<<<<<<<<<<[ INTRODUCTION TO SETS ]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# SETS ARE ALSO THE COLLECTION OF DATA BUT THE DIFFERENCE IS THAT SETS ARE NOT ORDERED IT IS RANDOM.......!
# in sets there are no key value pairs here there is just the keys no values..!


# a={"apple","abc",23}
# print(type(a))
# print(a)
# print(a[0])    # this give the error because there is no concept of order in the sets!
# print(a["abc"])  # this give error because there is no concept of values corresponding to keys in the sets..!


# # print("abc" in a)
# # print(21 in a)


# # for in sets:
# for v in a:
#     print(v)       # there is no logic of order in the sets..!


# #length of sets:
# # print(len(a))



# # add or update data in the sets..!
# a.add("temp")
# # print(a)

# b={"abc","t","ghi"}
# a.update(b)
# print(a)


# # #deletion of data
# a.remove("temp")
# print(a)

# # a.remove("skr")
# # print(a)            # it will give you the key error because "skr" is not present in the set.!


# a.discard(23)     # remove "23" from the set!
# print(a)

# a.discard("rrr")
# print(a)

# # note:----> there is a difference in "discard" and "remove" if you want to remove the key which is not present in the set
# #            then you will get a key error but in case of discard if u want to remove the key which is not present in the set
# #            then you will not get an error , it doesnot do anything and just returns.......!!!!!!!!!!!

# a.pop()     # it just remove one element from the set which element you cant say it just remove one element thats it......!!!!!!
# print(a)

# a.clear()    # it will clear the set!!!!!!!!!!
# print(a)

# del a         # it will delete the set itself!!!!!!!!!!!!!!!!!!



#- -  - - - - - - - - - -  - - - - - - - - - - -- - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#- -  - - - - - - - - - -  - - - - - - - - - - -- - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

#                  <<<<<<<<<<<<<<<<<<<<<[ FUNCTIONS RELATED TO THE SETS]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# a={1,2,3,4}
# b={3,4,5,6}

# a.update([1,2,3])=====> add the list passed to the set................!!!!!!
# we can do union as A|B and intersection as A&B...........!
# a.remove(5)================> remove 5 form the set a

# c=a.intersection(b)  # it gives the intersection of "a" with "b" !
# print(c)

# d=a.union(b)     # it gives the union of "a" with "b"..!
# print(d)


# e=a.difference(b)      # it gives everything that is on "a" but not on "b"...!!! ( very very important logic !)
# print(e)

# f=b.difference(a)
# print(f)

# g=a.symmetric_difference(b)   # this means the value which is not in the intersection of a and b is symmetric difference..!
# print(g)

# h=b.symmetric_difference(a)
# print(h)

# a.intersection_update(b)    # a has been updated with the intersection of "a" and "b"..!
# print(a)

# a.difference_update(b)
# print(a)

# a.symmetric_difference_update(b)
# print(a)

# note:--- there is no union_update() function ..!

# i=a.issubset(b)  # wehther "a" is the subset of "b"...!!
# print(i)


# c={3,4}
# d={7,8}
# print(a.issubset(b))
# print(a.issubset(c))
# print(c.issubset(a))
# print(a.issuperset(c))
# print(a.isdisjoint(c))
# print(a.isdisjoint(d))    # disjoint is true when there is nothing as common else it give false...!

#- -  - - - - - - - - - -  - - - - - - - - - - -- - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# note:----
# s={1,2,3,4,5,4,2,3,1}
# print(len(s),end="")
# s.add(4)
# s.add(3)
# print(len(s))
# note:-------- if there is repetition of elements in the sets then it count only once not again and again..
#               and if we add something that is already available in the set again it become common so it will also
#              not count again............ and it will also print the set having only unique values.....!!!!

# therefore it we get the ans as 5 and 5 in the above problems.............!!!!



#- -  - - - - - - - - - -  - - - - - - - - - - -- - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#- -  - - - - - - - - - -  - - - - - - - - - - -- - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

#             <<<<<<<<<<<<<<<[ SUM OF ALL UNIQUE NUMBERS IN A LIST ]>>>>>>>>>>>>>>>>>>>>>

# a={1,2,3,1,3}
# print(len(a))
# print(a)
# a.add(2)
# print(a)

#note:-------- if there is repetition of elements in the sets then it count only once not again and again..
#               and if we add something that is already available in the set again it become common so it will also
#              not count again............ and it will also print the set having only unique values.....!!!!


# def sumUnique(l):                            #(important logic)
#     s=set()       # way to make an empty set because if we use s={} it will be a dictionary not set........!!!!!!!
#     for i in l:
#         s.add(i)
#     sum=0
#     for i in s:
#         sum=sum+i
#     return sum

# print(sumUnique([1,2,3,4,4,3,4,2,1,5,5]))
