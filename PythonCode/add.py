class Add:
    def __init__(self):
        self.add_res=None
    def add_2_numbers(self,num1,num2):
        self.add_res=num1+num2
        return self

if __name__=="__main__":
    a=Add()
    print "## Instance of Class Add() is {}".format(a)
    x=a.add_2_numbers(10,20)
    print "Result of Addition is:{}".format(a.add_res)
    print "Value of Self is:{}".format(x)