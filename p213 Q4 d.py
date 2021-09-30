mylist=[19,87,1,-1,11,0,-1,33,19]
def binary_search_loop(listin,key):
    first=0
    last=len(listin)-1
    while last-first>=0:
        middle=first+((last-first)//2)
        if listin[middle]==key:
            return middle
        elif key<listin[middle]:
            last=middle-1
        else:
            first=middle+1
    return -1
print(binary_search_loop(mylist,-1))
print(binary_search_loop(mylist,33))
print(binary_search_loop(mylist,117))