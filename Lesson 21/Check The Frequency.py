testdic = {"My":1,"Name":2,"Is":1,"Archit":2,"Khanna":1}

print("The original Dictionary:", testdic)

v = 1

count = 0

for key in testdic:
    if testdic[key] == v:
        count = count + 1
print("The frequency of",v,"is:",count)