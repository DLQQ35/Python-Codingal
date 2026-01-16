set1 = {'A', 'B', 'C', 'D', 'E'}
set2 = {'B', 'D', 'V', 'X', 'Y', 'Z'}

union = set1.union(set2)
total_guests = list(union)

print("Total number of unique guests invited at the party:", len(total_guests))
print("Guests List:", total_guests)