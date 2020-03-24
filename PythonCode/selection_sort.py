def selectionsort(l1):
    for n1 in range(len(l1)):
        for n2 in range(n1,len(l1)):
            if l1[n1]>l1[n2]:
                l1[n1],l1[n2]=l1[n2],l1[n1]
    return l1

def reverseselectionsort(l1):
    for n1 in range(len(l1)):
        for n2 in range(n1,len(l1)):
            if l1[n1]<l1[n2]:
                l1[n1],l1[n2]=l1[n2],l1[n1]
    return l1

if __name__=="__main__":
    my_list=[1,10,2,9,3,8,4,7,5,6]
    print "** Unsorted List:{}".format(my_list)
    print "** Executing Selection Sort: **"
    print '** Sorted List:{}'.format(selectionsort(my_list))
    print "** Executing Reverse Selection Sort: **"
    print '** Sorted List:{}'.format(reverseselectionsort(my_list))

