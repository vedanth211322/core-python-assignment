def calculate_average(marks):
    return sum(marks) / len(marks) if marks else 0

def get_top_performer(students):
    averages = {student: calculate_average(marks) for student, marks in students.items()}
    top_performer = max(averages, key=averages.get)
    return averages, top_performer

students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}

averages, top_performer = get_top_performer(students)

print("Average Marks:", {student: round(average, 2) for student, average in averages.items()})
print("Top Performer:", top_performer)
