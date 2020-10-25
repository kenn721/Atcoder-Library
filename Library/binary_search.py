
#! binary search
#! 一致するものを探す
def binary_search(array,item):
    head = 0
    tail = len(array)-1
    while head<=tail:
        mid = (head+tail)//2
        if array[mid]==item:
            return mid
        if array[mid]<item:
            head = mid+1
        else:
            tail = mid-1
    return None