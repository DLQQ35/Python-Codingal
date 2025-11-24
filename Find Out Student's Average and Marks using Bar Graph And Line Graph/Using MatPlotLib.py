import matplotlib.pyplot as plt

student = ["Alice", "Bob", "Charlie", "David", "Eva","Balani"]

student_marks = [75, 60, 12, 9, 46, 67]

marks_percentage = []

for x in student_marks:
    res = (x / 80) * 100
    marks_percentage.append(res)
    print("The percentage of students marks are:", marks_percentage)

def marks_line_chart():
    plt.plot(student, student_marks)
    plt.title("Student Marks Line Graph")
    plt.xlabel("Students")
    plt.ylabel("Marks Obtained")
    plt.show()
marks_line_chart()

def percentage_bar_chart():
    plt.bar(student, marks_percentage)
    plt.title("Student Percentage Bar Graph")
    plt.xlabel("Students")
    plt.ylabel("Percentage Obtained")
    plt.show()
percentage_bar_chart()