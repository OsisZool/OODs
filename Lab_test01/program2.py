class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
            self.size = len(self.items)
    def push(self, i):
        self.items.append(i)    
    
    def pop(self): 
        o=0
        c=0
        for i in self.items :
            if i == ")" :
                c += 1
            elif i == "(" :
                o += 1
        self.items.pop()
        if o == c :
            return True
        else : 
            return False
  
  

s = Stack()
data = input("Enter math expression : ")
for i in data :
  s.push(i)

# print(s.items)
print(s.pop())
# for i in range(len(s.items)) :
#   print(s.pop())
# print(s.items)
# print(s.checkParentheses())