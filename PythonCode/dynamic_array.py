class DynamicArray:
    """ A Dynamic Array class akin to a simplified Python List. """

    def __init__(self):
        """ Create an empty Array. """
        self.n=0
        self.capacity=1
        self.A=self.make_array(self.capacity)

    def __len__(self):
        return self.n
    
    def __getitem__(self,k):
        if not 0 <= k <=self.n:
            raise IndexError ("Invalid Index")
        return self.A[k]