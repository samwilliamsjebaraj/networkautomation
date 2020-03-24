class MathOperations:
    ''' Performs Math Operations 
    1. Addition
    2. Subtraction
    3. Division
    4. Multiplication '''
    def add(self,a,b):
        ''' add(n1,n2) performs addition on n1 and n2 and returns n1+n2 '''
        if (type(a)==int or type(a)==float) and (type(b)==int or type(b)==float):
            return a+b
        else:
            return "Unsupported Input {}:{} {}:{}".format(a,type(a),b,type(b))
    def sub(self,a,b):
        ''' sub(n1,n2) performs addition on n1 and n2 and returns n1-n2 '''
        if (type(a)==int or type(a)==float) and (type(b)==int or type(b)==float):
            return a-b
        else:
            return ("Unsupported Input {}:{} {}:{}".format(a,type(a),b,type(b)))
    def mul(self,a,b):
        ''' mul(n1,n2) performs addition on n1 and n2 and returns n1*n2 '''
        if (type(a)==int or type(a)==float) and (type(b)==int or type(b)==float):
            return a*b
        else:
            return ("Unsupported Input {}:{} {}:{}".format(a,type(a),b,type(b)))
    def div(self,a,b):
        ''' div(n1,n2) performs addition on n1 and n2 and returns n1/n2 '''
        if (type(a)==int or type(a)==float) and (type(b)==int or type(b)==float):
            if b!=0:
                return a/b
            else:
                return "Division by 0 is not possible"
        else:
            return ("Unsupported Input {}:{} {}:{}".format(a,type(a),b,type(b)))

if __name__=="__main__":
    mo=MathOperations()
    print mo.add(5,'a')
    print mo.sub(5,4)
    print mo.mul(5,1001)
    print mo.div(5,'b')
