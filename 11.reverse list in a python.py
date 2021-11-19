# <<<<<<<<<<<<<<<<<<[ Reversing a list on python programming]>>>>>>>>>>>>>>>>>>>>>>>>>.

# def reverse_li(li1):
#     length=len(li)
#     for i  in range (int(length/2)):                       #[VERY VERY IMPORTANT CONCEPT]
#         li[i],li[length-i-1]=li[length-i-1],li[i]          #NOTE:--- for swapping a and b we write in python generally
#                                                            #[a,b=b,a] it means swap a with b and b with a!!!!!!!!!!!


# li=[1,2,3,4,5,6]
# reverse_li(li)
# print(li)

#-- -  - - - - -  - -  - -  - - -  -   - - - - - -  - - - -  - - - - -  - - - -  - - - - - - -  - - - - - - -  - - -  --  - - -


# by using negative index concept.......!!!!!!!!!!!!!
# def reverse_li(li1):
#     length=len(li)
#     for i  in range (int(length/2)):                       #[VERY VERY IMPORTANT CONCEPT]
#         li[i],li[-i-1]=li[-i-1],li[i]          #NOTE:--- for swapping a and b we write in python generally
#                                                            #[a,b=b,a] it means swap a with b and b with a!!!!!!!!!!!

# li=[1,2,3,4,5,6]
# reverse_li(li)
# print(li)
# print(li[3:1:-1])    # here step is "-1" so we go in backward direction............!!!!!!!! ( it will start from 3 and go upto 2)
# print(li[:1:-1])     # it will start from the end  and go upto 2 in backward direction
# print(li[3::-1])     # it will start from 3 and go upto first index element in backward direction....!!!
# print(li[::-1])  # this will start from end index and go upto first index  in backward direction!! ( also use for swapping list)
                   # and it will return a new list..........!!!!!!!

#-- -  - - - - -  - -  - -  - - -  -   - - - - - -  - - - -  - - - - -  - - - -  - - - - - - -  - - - - - - -  - - -  --  - - -


# swapping by slicing concept!!!
li=[1,2,3,4,5,6]
li=li[::-1]              # it will swap the list and give the swapped list as output of li............!!!!!!!!!!1
print(li)