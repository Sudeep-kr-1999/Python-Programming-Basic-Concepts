# <<<<<<<<<<<<<<<[ BINARY SEARCH PROGRAMME IN PYTHON]>>>>>>>>>>>>>>>>>>>>>>>>>>

# CONDITIONS FOR BINARY SEARCH:-----------------
# binary search simply means search the number by dividing whole array in two portion one is before mid and other is after mid 
# again and again...........................!!! till the number is found!!!!!!!!!!!!

# 1. THE GIVEN ARRAY MUSH BE SORTED..!


# def binarysearch(arr1,ele):
#     start=0
#     end=len(arr1)-1
#     while(start<=end):
#         mid=int(((start+end)/2))

#         if arr[mid]==ele:
#             return mid

#         elif arr[mid]<ele:
#             start=mid+1
#         else:
#             end=mid-1
#     return(-1)

# print("enter the number to search in the array : ",end=" ")
# n=int(input())
# a=n
# arr=[1,3,8,9,11,13,70,89,98]
# index=binarysearch(arr,a)
# print("the index of the searched number if available in the array is : ", index)



#- -  - - - -  - -  - -  - -  - -  - - - -  - - -  - - -- - - - -  - - - - - - - - -  - - - - - - -  - - - - - -  - - - -  -

# <<<<<<<<<<<<<<<<<<<<<[ SELECTION SORT CONCEPT OR ALGORITHM]>>>>>>>>>>>>>>>>>>>>>!!

def selectionsort(arr1):
    length=len(arr1)
        # put the correct element at ith position!!!!!!!!!

    for i in range (length-1):
        minindex=i

        #    calculating  the index of minimum element for this iteration...............!!!!!!!!!
        for j in range(i+1,length):
            if(arr1[j]<arr1[minindex]):
                minindex=j
            arr1[i],arr1[minindex]=arr1[minindex],arr1[i]        # for swapping..........!!!!!!!!


arr=[1,3,2,4,0,6,8]
selectionsort(arr)
print("The sorted array by selection sort is :",arr)


#- -  - - - -  - -  - -  - -  - -  - - - -  - - -  - - -- - - - -  - - - - - - - - -  - - - - - - -  - - - - - -  - - - -  -

# <<<<<<<<<<<<<<<<[ BUBBLE SORT CONCEPT OR ALGORITHM]>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def bubble_sort(arr1):
    length=len(arr1)
    # i is for n-1 rounds
    # j is for each iteration you need to go till (length-(i+1)) position.

    for i in range(length-1):  # jitna baar loop chalega.........!!!!
        for j in range(length-(i+1)):
            if arr1[j]>arr1[j+1]:
                arr1[j],arr1[j+1]=arr1[j+1],arr1[j]     # for swapping!!!!!!!!!!!!!!!!!


arr=[6,4,5,2,1,7,3]
bubble_sort(arr)
print("the sorted array by using bubble sort is : ",arr)


#- -  - - - -  - -  - -  - -  - -  - - - -  - - -  - - -- - - - -  - - - - - - - - -  - - - - - - -  - - - - - -  - - - -  -
# # <<<<<<<<<<<<<<<<[ INSERTION SORT CONCEPT OR ALGORITHM]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def insertion_sort(arr1):
    length=len(arr1)
    for i in range(1,length):
        j=i-1
        temp=arr1[i]
        #shifting element till this condition holds..
        while(j>=0 and arr1[j]>temp):
            arr1[j+1]=arr1[j]
            j=j-1
            #j+1 is the correct position for ith element
        arr1[j+1]=temp



arr=[9,8,5,6,7,1]
insertion_sort(arr)
print(arr)

#- -  - - - -  - -  - -  - -  - -  - - - -  - - -  - - -- - - - -  - - - - - - - - -  - - - - - - -  - - - - - -  - - - -  -

# <<<<<<<<<<<<<<<<<[ MERGE TWO SORTED ARRAY]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# def mergetwoarray(arr1, arr2):
#     i=0
#     j=0
#     len1=len(arr1)
#     len2=len(arr2)
#     arr=[]
#     while (i<len1 and j<len2):
#         if(arr1[i]<arr2[j]):
#             arr.append(arr1[i])
#             i=i+1

#         else:
#             arr.append(arr2[j])
#             j=j+1

#     while(i<len1):
#         arr.append(arr1[i])
#         i=i+1

#     while(j<len2):
#         arr.append(arr2[j])
#         j=j+1
#     return arr


# arr1=[1,4,9,10]
# arr2=[2,3,6,7,8]
# arr=mergetwoarray(arr1,arr2)
# print(arr)