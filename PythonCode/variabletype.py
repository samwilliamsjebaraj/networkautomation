class VariableType(object):
    @classmethod
    def main(cls,args):
        maxInt=sys.maxint
        longstart=maxInt+1
        floatvalue=0.1
        str1="hello world"
        print "type of maxInt",type(maxInt),"Value :",maxInt
        print "type of longstart", type(longstart),"Value :",longstart
        print "type of float value", type(floatvalue),"Value :",floatvalue
        print "type of str", type(str1),"Value :", str1

if __name__=="__main__":
    import sys
    VariableType.main(sys.argv)
