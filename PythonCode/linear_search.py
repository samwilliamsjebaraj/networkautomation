def linear_search(item,a):
    n=len(a)
    i=0
    while (i<n):
        if a[i]==item:
            return "The Item you Searched is found in index {} of the list".format(i)
        i+=1
    return "The Item you Searched is not in the list"

if __name__=="__main__":
    a1=[101,102,103,121,145,678,987,10987,12345,111,234,344,678,98]
    search_me=linear_search(98,a1)
    print search_me