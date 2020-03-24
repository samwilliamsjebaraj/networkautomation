def bubblesort(l1):
    swap_happened=True
    while swap_happened:
        swap_happened=False
        for x in range(len(l1)-1):
            if l1[x]>l1[x+1]:
                l1[x],l1[x+1]=l1[x+1],l1[x]
                swap_happened=True
    return l1

if __name__=="__main__":
    my_list=[10,1,9,2,8,3,7,4,6,5]
    print (my_list)
    sorted_list=bubblesort(my_list)
    print (sorted_list)