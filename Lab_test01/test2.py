class Stack :
    def push (self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
            self.size = len(self.items)
    def push(self, i):
        self.items.append(i)
    
    