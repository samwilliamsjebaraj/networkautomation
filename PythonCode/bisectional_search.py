class BisectionalSearch(object):
    def search(self,element,l):
        l.sort()
        start=0
        end=len(l)-1
        mid=(start+end)/2
        print l
        while mid<len(l):
            if l[mid]==element:
                return "{} Found in index {}".format(element,mid)
            elif element<mid:
                end=mid-1
            elif element>mid:
                start=mid+1
            else:
                return "{} not Found".format(element)
if __name__=="__main__":
    a=[10,6,7,3,5,2,2,0]
    bs=BisectionalSearch()
    print bs.search(2,a)