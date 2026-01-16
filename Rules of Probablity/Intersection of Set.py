set1 = {'A', 'B', 'C', 'D', 'E'}
set2 = {'B', 'D', 'V', 'X', 'Y', 'Z'}

intersection = set1.intersection(set2)
total_guests = list(intersection)

print("Total number of guests to be invited in party:", len(total_guests))
print("Guests List:", total_guests)