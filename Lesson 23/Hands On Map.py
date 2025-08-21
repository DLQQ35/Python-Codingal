number_1 = [1,2,3,4]
number_2 = [5,6,7,8]

result = map(lambda x,y : x+y,number_1,number_2)

print("The additions of two lists in ascending order starting for 1 to 8 is:")
print(list(result))

num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

def sq(n):
    return n*n

square = list(map(sq,num))

print("The squares of numbers from 1 to 30 is:")
print(square)