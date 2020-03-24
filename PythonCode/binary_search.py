def binary_search(item,list):
    '''
    please note the list must be sorted
    for the binary search to work
    '''
    print list
    list.sort()
    print list
    high=len(list)-1
    low=0
    while (low<=high):
        mid=(low+high)/2
        if list[mid]<item:
            low=mid+1
        elif list[mid]>item:
            high=mid-1
        elif list[mid]==item:
            return mid
    return None
if __name__=="__main__":
    l1=[10,3,5,6,2,8,100,101,1000,20002]
    i=10009
    a=binary_search(i,l1)
    print a
    