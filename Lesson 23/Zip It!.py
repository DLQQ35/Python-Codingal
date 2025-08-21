s1 = [1,2,3]
s2 = ["b","a","c"]
s3 = list(zip(s1,s2))
print(s3)


list_1 = [10,20,30,40,50]
list_2 = [100,200,300,400,500]

for x,y in zip(list_1,list_2[::-1]):
    print(x,y)


stocks = ["Reliance","Infosys","TCS"]
prices = ["12321","45611","97235"]

newdict = {stocks : prices for stocks,prices in zip(stocks,prices)}
print(newdict)