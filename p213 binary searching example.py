mylist=[17,24,45,31,50,63,85,96]
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
print(binary_search_loop(mylist,31))