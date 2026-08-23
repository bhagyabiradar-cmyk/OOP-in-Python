# List and Tuple combined

students = ["Bhagya", "Anu", "Ravi"]       # List
marks = (85, 90, 78)                       # Tuple

print("Students:", students)
print("Marks:", marks)

# Access elements
print("First student:", students[0])
print("First mark:", marks[0])

# Add to list
students.append("Priya")

print("Updated students:", students)

# Convert tuple to list
marks_list = list(marks)
marks_list.append(95)

print("Updated marks:", marks_list)

# Convert list back to tuple
marks_tuple = tuple(marks_list)

print("Final marks tuple:", marks_tuple)