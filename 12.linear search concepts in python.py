#<<<<<<<<<<<<<<<<<<<<[ LINEAR SEARCH CONCEPT IN PYTHON PROGRAMMING]>>>>>>>>>>>>>>>>>>>>>>>>

# Ques:----- search the given number in list and if it is present in the list then print the index number of that element
#            and if it is not present in the list then just print "-1 " as output!!!!!!!!!!

# n=int(input())

# li=[int(x) for x in input().split()]
# print(li)

# search=int(input())

# is_found=False

# for i in range(len(li)):
#     if li[i]==search:
#         print(i)
#         is_found=True
#         break

# if is_found is False:
#     print(-1)



# - - - -  - -  - - - -  - - -  - - - -  - - - -  - - - -  - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - - -
# <<<<<<<<<<<<<<<<[ LINEAR SEARCH WITH THE HELP OF FUNCTIONS ]>>>>>>>>>>>>>>>>>>>>>>>..

def linear_search(li,ele):
    #li is the list and ele is the element to search!!!

    for i in range(len(li)):
        if li[i]==ele:
            return i
    return(-1)


n=int(input())         # here n is the number to search in the list.........!!!!!!!!!!
a=n
li=[1,2,3,4,5]
index=linear_search(li,a)
print(index)
 #note: ------ here linear seach is first required the list and the element we have to search so we have to paas both the list
#              and the number to search as a parameter to the linear search function.............!!!!!!!!!!!1

