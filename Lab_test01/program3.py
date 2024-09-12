def findKeyword(str,keyword):
    slist = []
    klist = []
    for i in str:
        slist.append(i)
    for i in keyword:
        klist.append(i)
    if keyword in str :
        
        return True
    else :
        return -1


text = input("input String : ")
kw = input("input Keyword : ")
print(findKeyword(text,kw))


