class branching(object):
    def __init__(self,a):
        self.a=a
    def get_num_type(self):
        if self.a%2==0:
            return "Even Number"
        else:
            return "ODD Number"
    def __str__(self):
        return "branching: The Number:{} is an {}".format(self.a,self.get_num_type())

if __name__=="__main__":
    b=branching(10)
    print b.get_num_type()
    print b
    print b.__dict__