import math
class Queue:
    def __init__(self,list =None,list1 =None ) :
        if list == None:
            self.items = []
            self.items2 = []
        else:
            self.items = list
            self.items = list1
    def enQueue1(self,i):
        self.items.append(i)
    
    def enQueue2(self,i):
        self.items2.append(i)
    

q = Queue()
data = input("Enter you string : ")
s = math.floor(len(data)/2)
c=0

# if c < s :
#     for i in data:
#         q.enQueue1(i)
#         c+=1
# else :
#     for i in data:
#         q.enQueue2(i)
#         c+=1

# for i in range(len(data)):
#     i = 0
#     if i%2 == 0 :
#         print(q.items)
#     else :
#         print(q.items2())

# for i in range(len(data)) :
#     print(q.shuffle())

# print(q.items)
# print(q.shuffle())
# print(q.size())




# def findKeyword(text, keyword):
#     index = text.find(keyword)
#     if index != -1:
#         return index
#     else:
#         return None

# text = input("input String: ")
# kw = input("input Keyword: ")
# result = findKeyword(text, kw)

# if result is not None:
#     print(f"Keyword '{kw}' found at index: {result}")
# else:
#     print(f"Keyword '{kw}' not found in the input string.")
