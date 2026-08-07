num_subjects = int(input("Enter the number of subjects: "))

total_marks = 0

for i in range(1, num_subjects + 1):
    marks = float(input(f"Enter marks for subject {i}: "))
    total_marks += marks

percentage = (total_marks / (num_subjects * 100)) * 100

print("\nResult")
print(f"Total marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")