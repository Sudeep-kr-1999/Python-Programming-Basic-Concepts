# <<<<<<<<<<<<<<<<<<<<<<[ STRING CONCEPT IN PYTHON PROGRAMMING]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# (from string import * ) ----> for all the string function to import

from string import *
str="sudeep"
print(str.isalpha())
# str.isa

# 1. STIRNG:---- it is a sequence of characters

# 2. STRING:---- it is a sequence of unique codes actually like ASCII codes in java anc c++ ( internally).

# s="Sudeep"
# print(s)

# k='SUDEEP'
# print(k)

# r='''sudeep'''
# print(r)


# double quote and single quote will only allow you to print the string in only a single line!!!!!!

# if we want to enter string in multiline then triple quotes is very much helpful for that !!!( very very important notes)..!!

# a="my name
# is sudeep
# kumar"

# print(a)

# the above code will not work properly for double quote and single quote but if we do the same in triple quote it will work fine!

# a='''my name
# is sudeeep
# kumar'''

# print(a)


# s="sudeep"
# # accessing elemnts of string with the help of indexing.#####
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[4])
# print(s[5])
# print()
# print()

# # negative indexing is also present into the string..........!!!!!!!!
# print(s[-1])
# print(s[-2])
# print(s[-3])
# print(s[-4])
# print(s[-5])
# print(s[-6])


# s='''My
# Name Is
# Parikh'''

# print(s[2])    # it is a end line charcter which we can see in the terminal with a  blank space...!!
# print(s)

# - - - - -  -  - -  - - -  - - -  - - - -  - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                            #    <<<<<<<<<<<[ how strings are stored]>>>>>>>>>>>>>>>>>>>>.
# s="Parikh"
# print(id(s))    #  "S" it will store the refrence of Parikh

# a="Rohan"
# print(id(a))    #  "a" it will store the refrence if Rohan

# a="Parikh"      # at this point the refrence of "a' and "s" are same!
# print(id(a))


# note:-------- STRINGS ARE IMMUTABLE IN PYTHON...............!!!!!!!!

# a="Parikh"
# print(a[0])
# #a[0]=R             # we can access the element by their index number but we cannot change the value of any element of the string
#                    # at any index as we are doing in the case of lists........so string are immutable.......!!!! we can only
#                 # change the refrences................!!!!!!!!!!!!!!!!
# print(a)


# - - - - -  -  - -  - - -  - - -  - - - -  - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

                # <<<<<<<<<<<<<<<<<<<<<<[ CONCATENATION OF STRINGS]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# CONCATENATION OF STRINGS:------------ it generally means joining 2 or more strings( HAPPEN USING + OPERATOR)................!!!!

# a="red"
# print(id(a))
# a=a+"blue"
# print(a)
# print(id(a))
# a=a+"red"+"green"+"black"
# print(a)
# print(id(a))
# a+="blue"
# print(a)
# print(id(a))

# note:-------  above the id of every output is different from each other. because string are immutable means every time a new
#               string is created after concatenation and then "a" change its reference to that ......... means there is no
#               change in the previous version of "a" ........!!!!!!!!!!!!!


# a="red"
# print(a)
# print(id(a))
# a=a*14         # the "a*14" means a is repeated 14 time in the string i.e "a=a+a+a............upto 14 times"....!
# print(a)
# print(id(a))

# generally :-----# "a*n" means a will be appended "n-1" times with a to complete the strings and the complete length has "n" times
                    # "a" with it..................!!!!!!!!!!!!!!

# a="red"
# a=a+3              # note:---- if we append string with a number then it show a error !!!!!!!!!!!!!!!!!
# print(a)           #           because python donot know how to add string with an integer.............!!!!!!!
                  #  if we have to do this then we have to typecast the interger to a string by using inbuilt function "str"....!!


# the below code will work fine because the integer is typecasted to a string with the help of "str" function.......!!!
# a="red"
# a=a+str(3)
# print(a)

# - - - - -  -  - -  - - -  - - -  - - - -  - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                        # <<<<<<<<<<<<<<<<<[ SLICING OF STRING]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# s="Parikh"
# print(s)

# print(s[1:4])
# print(s[1:4:2])
# print(s[6:4])   # this will show a empty string....!!!!!!
# print(s[-1])
# print(s[-5:-3])
# print(s[1:])
# print(s[:4])
# print(s[1:9])
# print(s[4:1:-1])
# print(s[5::-1])
# print(s[:2:-1])

# note:------- all the outputs coming after slicing is  itself a new string because strings are immutable..!
#  NOTE:---->> Agar backward jaaayege to end ke ek aage rukege aur agar forward jaayege to end ke ek piche rukege.............!!!!!!


# - - - - -  -  - -  - - -  - - -  - - - -  - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                     # <<<<<<<<<<<<<<<<<<<[ITTERATION ON STRINGS ]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# HOW TO ITERATE ON STRING!!!!!!!!!!

# str="Hello World"
# print(str)


# # calculate how many times "l" appears in the string....!!??
# count=0
# for letter in str:
#     if letter=='l':
#         count=count+1
# print("number of times 'l' appears in the string is :",count)


# count1=0
    # for i in range(len(str)):
#     if(str[i]=='l'):
#         count1=count1+1
# print("number of times 'l' appears in the string is :",count1)

               # <<<<<<<<<<<<<<<<<<<<<<[( in and not in) OPERATION IN THE STRING]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# (in and not in):  " in "operator  checks wether a string is a substring ........!!!
#                  " not in " operator will check wether this is not a substring.......!!!!!
# note:-----> for substring you cannot skip any character in the string...if you do so it is not considered as substring..!
#   note:------> you have to go only to the right direction or you can say forward direction for finding substring..!


# str="hello"

# # application of "in" operator in string !
# # if "hel" in str:
# #     print("yes it is a substring")
# # else:
# #     print("not a substring")


# # application of "not in" operator in the string!!!!
# if"hllo" not in str:
#     print("yes it is not a substring")
# else:
#     print("it is a string")

# - - - - -  -  - -  - - -  - - -  - - - -  - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # <<<<<<<<<<<<<<<<<<<<<[ COMPARISON OPERATIONS ON STRINGS]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# comparision operator( >=,<=,<,>,==,!= )

# a="Parikh"=="Parikh"
# print(a)     # give wether "a" is true or not!!

# b="Rarikh">="Parikh"
# print(b)
# note:----- these comparison are depends on ASCII values of characters and on the basics of ASCII values these are compared..!

# note:----- comparison mein ye ek string ke har position waale letter ko dushre string ke corresponding same position waale letter
#            se compare krta h aur jaise hi usse koi aisa position milta h jaha pr dono corresponding string ke same position  waale
#            letter ka ASCII value alag h uss position ke basic pr wo desicision leta hai ki comparison true hai ya false...!!!

# c="Pbrikh">="Parikh"
# print(c)

# d="parikh">="Parikh"
# print(d)

# e="par">="parikh"
# print(e)

# f="parikh">="par"
# print(f)

# g="parikh">="parikh"
# print(g)

# h="parikh">"parikh"
# print(h)

# i="parikh"!="parikh"
# print(i)

# j="par"!="parikh"
# print(j)

# k="abce">="abcdef"            # VERY IMPORTANT EXAMPLE ..!!!!!!!!!!!!!!
# print(k)


# - - - - -  -  - -  - - -  - - -  - - - -  - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - -  -  - -  - - -  - - -  - - - -  - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

                  #  <<<<<<<<<<<<<<<<[ OPERATION ON STRINGS]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# - - - - -  -  - -  - - -  - - -  - - - -  - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# functions of string............!!!
# # split function.........!!!!!
# str="My Name Is Parikh"


# split function.........!!!!!!!!!!!!

# li=str.split()
# # split function returns a list of string on the basis of de-limiter you pass... if you donot paas any delimiter it just take
# # "space" as a default delimiter and return a list.............!!!!
# print(li)

# str1="My,Name,Is,Parikh"
# print(str1)          # it will give you complete string as a element of the list because no delimiter is passed to string..!

# print(str1.split(','))   # it will give you list of string on the basis of delimiter passed that is ",".!

# print(str1.split(',',2))  # here the number you give as argument you will get a list which is splitted into one more item than the
#                          # number you passed .... here we pass "2" then we get a list which is splitted into 3 items.....!
# print(str1.split(',',0))
# print(str1.split(',',1))
# print(str1.split(',',3))
# print(str1.split(',',4))

# - - - - -  -  - -  - - -  - - -  - - - -  - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# replace function!!!!!!!!

# str="My Name Is Parikh"
# print(str.replace("Parikh","Rohan"))
# print(str)   # here string is not changing so the previous string will not change...!

# # replace function is used to replace something from some other thing in the string .
# # replace( paramaeter1, parameter2)  here the parameter1 is the thing to be replaced and the parameter2 is the thing by which
# #  it is replaced................!!!!!!!!!!!!!!!!!!

# print(str.replace("which","Rohan"))  # it will not do anything with the string because "which" is not present in the string......!!!

# str="My Name Is Parikh Parikh Parikh Parikh"
# # note if a element to be replaced is present multiple time in the string then all that element will be replaced in one go
# #      if we replace it with some element by default.....
# # for example:---------------------------> below is the example....>!!!

# print(str.replace("Parikh","Rohan"))

# # if we want that only the given number of elemment should replace not all as it is done in by default then we should give a
# # parameter (integer) as the third argument in the replace function so that it will replace as much the user want.....!!

# # for example:----------------------!

# print(str.replace("Parikh","Rohan",2))  # it will replace only 2 "Parikh" with "Rohan" starting from first.......!!!!!!!

# - - - - -  -  - -  - - -  - - -  - - - -  - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# find function.........!!  : it is used if you want to find something in the string...... !
# find function returns the index of the finding substring whereever it starts under the string.............!( very important)!

# str="My Name Is Parikh Parikh"
# index=str.find("Na")
# print(index)        # it actually returns the strarting index of the substring wherever it starts....!
#                    #  here in this case the starting index of "Na" is 3 because the index of "N" is 3.....!!!!!!!

# print(str.find("Nae"))    # it will return "-1" because it is ot a continuous string  so there is not a substring like that in
#                           # this parent string...........! ( note)..........!

#                           # index "-1" means string is not present because index starts from "0".!

# print(str.find("Par"))   # it will give you the index of first "Par" which will found in the string starting from first...!


# # if we want to find the index of substring in certain rannge of the string then we can do what is done in the below example!
# print(str.find("Par",16,21)) # in the part of the string which is going from the index 16 upto 20 we find the index of "Par"

# - - - - -  -  - -  - - -  - - -  - - - -  - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# lower and upper function in the string..!
# lower function:-- it is used to  convert the string into lower case....!!!
# Upper function:---- it is  used to convert the string into the upper case..!!!!!

# str="My Name Is Parikh"
# print(str)
# str1=str.lower()       #  convert whole string to lower case and return a new string ..!!!
# print(str1)
# print(str)
# str2=str.upper()       #  convert whole string to upper case and return a new string ..!!!
# print(str2)

# - - - - -  -  - -  - - -  - - -  - - - -  - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# "startswith() function".....................!
#  this function check wether the string starting with this substring or not...............!!!!!!!!!
# this function returns the boolean means "True" or "False".........!!!

# str="My Name Is Parikh"
# ans=str.startswith("My Na")
# print(ans)

# print(str.startswith("Is Pa",11,25))   # this means wether the part of the string starting from the index 11 and go upto 25 will
# #                                        starts with "Is Pa".............!!!!!!!!

# - - - - -  -  - -  - - -  - - -  - - - -  - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - -  -  - -  - - -  - - -  - - - -  - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - -  -  - -  - - -  - - -  - - - -  - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


#             <<<<<<<<<<<<<<<<<<<<<<<<[ Replacing characters in the string]>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# def replace(str,char1,char2):
#     newstr=""
#     for char in str:
#         if(char==char1):
#             newstr+=char2
#         else:
#             newstr+=char
#     return(newstr)

# str="fsafsavxz"
# str=replace(str,'s','d')   # this means in str string replace every occurence of s with d.
# print(str)


# note:--- here we cannot replace  the element of the string because string are immutable !!!!!!!!(very very important)!!!!!!!!!


# - - - - -  -  - -  - - -  - - -  - - - -  - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# <<<<<<<<<<<<<<<<<<<<<<[ COUNT VOVELS , CONSONANTS, DIGITS, AND SPECIAL CHARACTER IN THE STRING]>>>>>>>>>>>>>>
# def countinstring(str):
#    v, c, d, s = 0, 0, 0, 0
#    for char in str:
#         if (char >= 'a' and char <= 'z') or (char >= 'A'and char <= 'Z'):
#            char = char.lower()
#            if(char == 'a'or char == 'e'or char == 'i' or char == 'o' or char == 'u'):
#                v = v+1
#            else:
#                c = c+1
#         elif (char>='0'and char<='9'):
#             d+=1
#         else:
#             s+=1
#    return(v,c,d,s)

# str="sfsdfafdFFFAAAAHG 425346#@$%"
# v,c,d,s=countinstring(str)
# print(v,c,d,s)

# # here "v" is vovel !!!!!!
# # here "c" is consonants !!!!!!
# # here "d" is digits !!!!
# # here "s" is special character.!!!!!


# ======================================================================================================================================================================
#  taking input for multiline string (very very important):--------------------------

lines = []
while True:
    try:
        line = input()
        if line:
            lines.append(line)
    except:
        break
inp_str = '\n'.join(lines)

# ======================================================================================================================================================================
