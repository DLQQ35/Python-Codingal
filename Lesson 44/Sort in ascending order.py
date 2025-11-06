import numpy as np
data_type = [("name", "S15"), ("age", int), ("height", float)]

student_details = [("Alice", 21, 5.5), ("Bob", 22, 6.0), ("Charlie", 20, 5.8), ("David", 23, 5.9)]
students = np.array(student_details, dtype=data_type)

print("Original Array:")
print(students)

print("Sort by height:")
print(np.sort(students, order="height"))

print("Sort by age:")
print(np.sort(students, order="age"))

print("Sort by name:")
print(np.sort(students, order="name"))