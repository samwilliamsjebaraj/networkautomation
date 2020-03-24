class SuperList(list):
    def __len__(self):
        return 100


if __name__=="__main__":
    sl=SuperList()
    print (len(sl))
    sl.append("hello")
    print sl