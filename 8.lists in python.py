                                             #lists in python programming..!!!!!!!

# creating a list
# li=[]
# li=[1,2,3]
# print(type(li))

# li=[1,2,"parikh",3.4]

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 


                                          # ACCESS AND CHANGE ELEMENT IN THE LIST


# li=[1,2,"parikh",3.4]
# print(li[0])
# print(li[1])
# print(li[1])
# print(li[2])
# print(li[3])
# print(li[4])  #it will show out of range because that index is not avialable in the list.!


# li[0]=5
# print(li)

# note:--we can do operations with only those number which are in the range of list.

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 

                                           # SLICING OF THE LIST CONCEPT

# li=[1,2,"parikh",3.4]
# print(li[1:3])   # starting with one index and go upto 2 index.
# print(li[1:])      # starting from the first index till the last index..
# print(li[1:10])     # starting from 1 and go till  9 and if those many elments were nt present in the list it will stop at last element!

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 

                                         # insert and append element on the list!

li=[1,2,"parikh",3.4]
# li.append("Ankush")         # it will automatically append "Ankush" at the end of the list...!!!!
# print(li)

# syntax of insert function:-->> list.insert(index,value)...!!
li.insert(1,7)        # it will insert 7 at the first index of the list..!!!!
print(li)

# li.insert(6,10)
# print(li)

# li.insert(9, "karan")
# print(li)  #note:----- if we want to insert the element at that position which is not present in the list it will automatically
#                      # insert that element at the last position of the list...!!!!!!!!!!!!

# li.append([9,10,11])     # it will create a list object nd  append it on the last of the list..........!!!!!!
# print(li)


# li.extend([9,10,11])         # extend is used when we want to append multiple element in the list in on go,.............!!!!
# print(li)


# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 

                                     #removing element from the list


# li=[5,7,2,"parikh","rohan","Ankush",10,"karan", 9,10,11,5]
# li.remove(2)        # will remove 2 from the list..!!!!
# print(li)


# li.remove(5)
# print(li)       #note:--- if any element is present multiple times in the list then that element will be removed which will come
#                        # first in the list other will not remove .

#                        # for ex:-- here we want to remove 5 so that file will remove which will come first the five at the
#                              #     last position will not be removed...!

# # li.remove(6)         # it will show error that  6 is not present in the list so it cann't be removed.
# # print(li)


# c=li.pop()              # by default remove one element from the list but from the last positon (very very important)!
#                       # and it will return us the element which is deleted from the last position..!

# print(li)     #>>>>>>>>>>>> show that the last element is being deleted due to the use of pop() function.!
# print(c)      # >>>>>>>>>>>> it will return the elemnt which is being deleted...........!!!!!!!

# li.pop(2)        #now pop will remove the element from the index it is provided...>!!!!!!!!!!
# print(li)

# li.pop(18)   # if we gve that index to the pop to remove which is not in range of the list then it will show error
#             #  because we can delete only that element which are present on the list......!!!!!!!!! ( very very important)!
# print(li)


                   # length functionality of the list( it will tell you how many element is present in the list)



# li=[5,7,2,"parikh","rohan","Ankush",10,"karan", 9,10,11,5]
# c=len(li)             # it will return the length of the list( basically how many elements are present in the list)!
# print(c)


# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<[ how elements are stored in the list]>>>>>>>>>>>>>>>>>>>>>>>

# 1. lists Actally stores the references of the elements it doesnot store the elements directly it stores the references of that 
#    elements!!!!

# 2. references are stored in a contiguous memory loacation

# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Looping on the list in python>>>>>>>>>>>>>>>>>>>>>

# li=[1,2,"Parikh",9,10,11,"Ankush"]
# print(li)


# for i in range (len(li)):    # the way of running a loop using indexing in the list in the python!!!
#     print(li[i])


# for i in range(2,len(li)):
#     print(li[i])q



# for ele in li:          # new way of printing element of list by using "ele" means element it means print elements in the list!
#     print(ele)            # it do not take index it directly print the list element............!!!!!!!!



# for ele in li[2:]:      #it will print the element from the index 2 to the end of the list due to slicing of the list!!!
#     print(ele)



# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - 

#<<<<<<<<<<<<<<<<<<<<<<<[ Negative index and sequencing list concept in python]>>>>>>>>>>>>>>>>>>>>>>

                            #   <<<<<<<# negative indexing in list...!!>>>>>>>>>>>>>>

# 1.generally if we use negative indexing it will start giving elements from the end of the list  instead of from start of the list.

# 2. negative indexing starts from "-1" and as we go to "-2 " or"-3" the index number will move backward from the last element
#   means in a opposite direction sense...........!!!!!!!!

# 3. and again if you want to go with negative list index out of range it will definitely show you a error saying that the 
#    list index you are using is out of range........!!!!!!!!!!!


# li=[1,2,3,4,5]
# print(li[0])
# print(li[-1])       # the index "-1 " will give the element from the last index of the list...!
# print(li[-2])
# print(li[-3])
# print(li[-8])        # this list index  is out of range of the list.!!!!!!!





                # <<<<<<<<<<<<<<<<<<<<[ SEQUENCING IN A LIST]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# 1. We want a part of the list and that part may be generated using sequence in the list....!!!

# 2. as for loop has a body ( for(start,end,step) ) similarly sequence in the list has also a syntax body which is:
#      (list[start:end:step])!

# li=[1,2,3,4,5]
# print(li)

# print(li[1:5:1])       # it will start the list from the index 1 and go upto 4th index taking step of 1 unit at once and finally
#                         # print the resultant list................!!!!!!!!!!!!!!!!


# print(li[1:])        # start from index 1 and go till the end of the list and step in by default 1.!!

# print(li[1::2])    # starting form index 1 of the list go till last and will increment by 2!!!
# print(li[:3])       # starting from 0 index goes upto  2 and by default step is 1 in this case....!

# print(li[-1:])        # my by default end is 5 means last element and we start form the last and by default step is only 1 so only
#                      #  last element prints in this case it is 5,....!

# print(li[-3:-1])      # going from -3 to -1 index and by default step is 1!!




# - - - - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -

                      #<<<<<<<<<<<<<<<<<<<<<<[ Taking inputs in a list]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# There are 2 ways of taking inputs in a list:--------
#1. LINE SEPRATED  INPUTS IN A LIST.......!!!!!

                #    <<<<<<<<<<<<<<<<<<<<[ LINE SEPRATED INPUTS IN A LIST]>>>>>>>>>>>>>>>>>>>>>>>

# n=int(input())      # total number of elements in the list.......!!!!!!!
# li=[]               # initialize with an empty list
# for i in range(n):
#     curr=int(input())
#     li.append(curr)

# print(li)

# # in this method we initialize with an empty list and then start taking numbers and finally append it to the list ....!!

# for ele in li:
#     print(ele)


# n=int(input())
# li=[]
# for i in range(n):
#     li.append(input())   # it will print string as the element of the string because int is not included with the input command!
# print(li)



                  # <<<<<<<<<<<<<<<<[ Space seprated input in the list]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# n=(input())
# print(n)
# print(type(n))

# str=input()
# print(str)
# print(type(str))

# li=[]
# string_split=str.split(' ')          # here is a split functionality which split anything on the basic of parameter given under
#                                       #brackets in this case string is spliting on the basic of space.........!!!!!!!!!!
#                                       # on the basic of which split function will work is called delimiter, in this case space.!
# print(string_split)


# str=input()
# str_split=str.split(",")
# print(str_split)


# li=[]
# str=input()                             #m<<<<<<[ very very important note]>>>>>>>>>>>>>>>>
# str_split=str.split()                  # by default split functionality is on the basis of space delimiter..........!!
# print(str_split)                       # this will be a list of string and we have to convert it into integer..!

# # for converting string into the integer for the above list which has string numbers as elements!!!!!
# for ele in str_split:
#     li.append(int(ele))

# print(li)        # this will give the list of integers................!!!!!!!



               # <<<<<<<<<<<<<<<<<<<[ Another way of doing that]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# li=[int(x) for x in input().split()]
# print(li)

# for ele in li:
#     print(ele)

# n=int(input())
# li=[int(x) for x in input().split()]
# print(li)
# for ele in li:
#     print(ele)


