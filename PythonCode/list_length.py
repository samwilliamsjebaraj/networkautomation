import sys
n=100
data = []
for k in range(n):
    a=len(data)
    b=sys.getsizeof(data)
    print ("Length:{0:3d}; size in bytes: {1:3d}".format(a,b))
    data.append(None)