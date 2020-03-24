def return_min_value(l1):
    ''' returns the min value of the equilibrium '''
    val_list=[]
    print "Length of list is {}".format(len(l1))
    ll=len(l1)
    print (l1[1:ll])
    print l1[0]
    min_diff_val=abs(sum(l1[1:ll])-l1[0])
    for pointer in range(1,(len(l1))):
        left_list=l1[0:pointer]
        print "LL:{}".format(left_list)
        right_list=l1[pointer:(ll)]
        print "RL:{}".format(right_list)
        x=abs(sum(left_list)-sum(right_list))
        if min_diff_val > x:
            min_diff_val=x
        else:
            pass

    return min_diff_val


if __name__=="__main__":
    l=[3,1,2,4,3]
    print l
    print return_min_value(l)