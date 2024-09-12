def findKeyword(s, keyword):
    slist = []
    for i in range(len(s) - len(keyword) + 1):
        if s[i:i + len(keyword)] == keyword:
            slist.append(i)
    return slist

text = input("input String: ")
kw = input("input Keyword: ")
print(findKeyword(text, kw))

