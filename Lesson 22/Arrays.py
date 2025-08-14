import array as ar

arraynum = ar.array('i', [1, 2, 3, 4, 5, 6, 3,3,3,3])
print("Original Array:",arraynum)

print("The number of occurence of the number 3 is:")
print(arraynum.count(3))

arraynum.reverse()
print("The reverse of the given array is:")
print(arraynum)