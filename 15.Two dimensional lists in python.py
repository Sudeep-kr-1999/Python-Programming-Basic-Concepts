#             <<<<<<<<<<<<<<<<<<<<<<[ TWO DIMENSIONAL LISTS IN PYTHON]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#- - - - - - - - - - - - - -- - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

#     <<<<<<<<<<<<<<<<<<<<<[ INTRODUCTION TO TWO DIMENSIONAL LISTS IN PYTHON]>>>>>>>>>>>>>>>>>>>>>>>>>>>

# li=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# print(li[2][2])
# print(li[2][3])
# print(li[2][5])   # it will not give any output because there is no fifth column in third row!!!

# li[2][2]=20
# print(li)


#- - - - - - - - - - - - - -- - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#            <<<<<<<<<<<<<<<<<<[ HOW TWO DIMENSIONAL LISTS ARE STORED]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# A 2-D list is actually the list of lists.........!!!!!!!
# li=[[1,2,3,4],[5,6,7,8]]
# print(type(li[0]))
# print(li[0][1])
# print(id(li))
# print(id(li[0]))
# print(id(li[1]))
# li[1]="PARIKH"
# print(li)


#- - - - - - - - - - - - - -- - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#               <<<<<<<<<<<<<<<<<<<<<<<<<[ JAGGED LIST CONCEPT ]>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# THE 2 DIMENSIONAL LISTS  OF DIFFERNT COLUMN SIZE IS GENERALLY CALLED JAGGED LIST....!
# THE TWO DIMENSIONAL LIST IS THE LIST OF LISTS BUT WE NEVER SAY FOR EACH LIST COLUMN SIZE IS ALSO SAME IT MAY VARRY.!

# li=[[1,2,3,4],[5,6,7],[8,9],[10,11]]
# print(li[0])
# print(li[2][3])  # it give index out of range because in the third list the third list is not available..!


#- - - - - - - - - - - - - -- - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            #    <<<<<<<<<<<<<<<<<[ LIST COMPREHENSION CONCEPT]>>>>>>>>>>>>>>>>>>>>>>>
# li=[1,2,3,4]

# li_new=[]

# for ele in li:
#     li_new.append(ele**2)
# print(li_new)


#  # ANOTHER WAY OF DOING THAT....!

# syntax:----- [output for expression (condition)]
# li_new=[ele**2 for ele in li]   # by using comprehension of lists.........!!!
# print(li_new)



# li_square_even=[ele**2 for ele in li if ele%2==0]
# print(li_square_even)


# li=[1,2,3,4]
# li_even_square=[]
# for ele in li:
#     if ele%2==0:
#         li_even_square.append(ele**2)

# print(li_even_square)



# li=[1,2,3,4,5,6,7,8,9]
# li_new=[]
# for ele in li:
#     if ele%2==0:
#         if ele%3==0:
#             li_new.append(ele)

# print(li_new)

#         # OR

# li_new=[ele for ele in li if ele%2==0 if ele%3==0]
# print(li_new)





# li_1=[1,2,3,4,5]
# li_2=[2,4,6,7]
# li_intersection=[]
# for ele_1 in li_1:
#     for ele_2 in li_2:
#         if ele_1==ele_2:
#             li_intersection.append(ele_1)
# print(li_intersection)


# li_intersection=[ele for ele in li_1 for ele2 in li_2 if ele==ele2]
# print(li_intersection)



#
# li=[1,2,3,4,5]
# li_inter=[ele**2 if ele%2==0 else ele for ele in li]
# print(li_inter)



# s="Parikh"
# li=[ele for ele in s ]
# print(li)


# very very important logic comprehension for 2d list........!!!
# li=["Parikh","Rohan","Ankush"]
# list_2d=[[s for s in ele] for ele in li]
# print(list_2d)



#- - - - - - - - - - - - - -- - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#              <<<<<<<<<<<<<<<<<<[ INPUTS OF TWO DIMENSIONAL LIST -1]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# str=input().split()
# # print(str)
# n,m=int(str[0]),int(str[1])

# li=[[int(j) for j in input().split()] for i in range(n)]
# print(li)

# INPUT SAMPLE:
# 3 4
# 1 2 3 4
# 7 6 7 8
# 9 10 11 12


# for jagged list no need to take input for number of columns:-
# str=input().split()
# n=int(input())
# li=[[int(j) for j in input().split()] for i in range(n)]
# print(li)

#- - - - - - - - - - - - - -- - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#              <<<<<<<<<<<<<<<<<<[ INPUTS OF TWO DIMENSIONAL LIST -2]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# NOTE:-----  for(i,j) element in the 2-D list the formula is  (m*i+j) !!!! ( very very important formula)

# take input in one line and the outputs in other line..............!!!
# str=input().split()
# n,m=int(str[0]),int(str[1])
# b=input().split()
# arr=[[int(b[m*i+j]) for j in range (m)] for i in range(n)]
# print(arr)



# # to take inputs of input and output in one line directly........!!
# str=input().split()
# n,m=int(str[0]),int(str[1])
# b=str[2:]
# arr=[[int(b[m*i+j]) for j in range (m)] for i in range(n)]
# print(arr)


#- - - - - - - - - - - - - -- - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# <<<<<<<<<<<<<<<<<<<<<<[ PRINTING TWO DIMENSIONAL LISTS ]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# li=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# n=3
# m=4
# for i in range(n):
#     for j in range(m):
#         print(li[i][j],end=" ")
#     print()




# li=[[1,2,3,4],[5,6],[9,10,11]]
# n=3
# for row in li:
#     for ele in row:          # the use of "in" operator to print the list...!
#         print(ele,end=" ")
#     print()


# <<<<<<<<<<<[ join function in string concept]>>>>>>>>>>>>>>>>>>>>

# str='ab'.join("abcd")   #join like : aabbabcabd.... do not join with the last element...!
#                         #   note:-- jisse join ho rha h aur jo join ho rha h dono string ke hone chahiye( in this case string)!
# print(str)


# str="ab".join(['1','2','3'])
# print(str)



# output of 2 dimensional lists by using join operator very very important!!!!!!!!!!!
# li=[[1,2,3,4],[5,6],[9,10,11]]
# n=3
# for row in li:
#    output=" ".join([  str(ele) for ele in row ] )
#    print(output)

# note:----------->> in this example space is joined with each element of the 2 dimensional list.............!!!!!




#- - - - - - - - - - - - - -- - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# <<<<<<<<<<<<<<<<<<<<<<[ LARGEST COLUMN SUM IN TWO DIMENSIONAL LISTS]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# QUES:- FIND THE INDEX OF THE COLUMN WHICH HAS THE LARGEST SUM AND IF 2 COLUMNS COMES TO BE THE LARGEST GIVE THE INDEX OF THE 
#         COLUMN ARRIVE FIRST............!!!!!!!!!!!!!!!

# def lar_call_sum(li):
#     n=len(li)
#     m=len(li[0])
#     max_sum=-1
#     max_col_index=-1
#     for j in range(m):
#         sum=0
#         for i in range(n):
#             sum+=li[i][j]
#         if sum>max_sum:
#             max_col_index=j
#             max_sum=sum
#     return max_sum,max_col_index



# li=[[1,2,3,4],[8,7,6,5],[9,10,11,12]]
# lar_sum,lar_col_index=lar_call_sum(li)
# print(lar_sum ,lar_col_index)


        #  ANOTHER WAY OF DOING THIS

# def lar_call_sum(li):
#     n=len(li)
#     m=len(li[0])
#     max_sum=-1
#     max_col_index=-1
#     for j in range(m):
#         sum=0
#         for ele in li:
#             sum+=ele[j]     #ele in li at j equals to position..........!!!!!!!
#         if sum>max_sum:
#             max_col_index=j
#             max_sum=sum
#     return max_sum,max_col_index



# li=[[1,2,3,4],[8,7,6,5],[9,10,11,12]]
# lar_sum,lar_col_index=lar_call_sum(li)
# print(lar_sum ,lar_col_index)
