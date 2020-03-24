def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

if __name__=="__main__":
    import time
    t=time.time()
    a=10
    b=5
    procs=[add(a,b),sub(a,b),mul(a,b),div(a,b)]
    for p in procs:
        print p
        p.start()
    for p in procs:
        p.join()
    print "Time taken {}".format(time.time()-t)