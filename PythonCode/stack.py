class Stack(object):
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self,item):
        if not is_empty(self):
            return self.items[-1]
        else:
            return 0

if __name__=="__main__":
    s=Stack()
    print s.is_empty()
    s.push("interface Gig0/0")
    s.push("ip address 10.1.1.1 255.255.255.255")
    s.push("service-policy ABC in")
    print s.is_empty()
    print s.items
    print s.pop()
    print s.items