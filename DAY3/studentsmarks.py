def calculate_grade(avg):
    if avg >= 90:
        return "A"
    if avg >= 80:
        return "B"
    if avg >= 70:
        return "C"
    if avg >= 60:
        return "D"
    return "F"

name = input("Enter student name: ").strip()

marks = []
while True:
    subject = input("Enter subject name (or 'done' to finish): ").strip()
    if subject.lower() == "done":
        break
    try:
        score = float(input(f"Enter marks for {subject}: ").strip())
    except ValueError:
        print("Please enter a valid number for marks.")
        continue
    marks.append((subject, score))

if not marks:
    print("No subjects entered.")
else:
    total = sum(score for _, score in marks)
    avg = total / len(marks)
    grade = calculate_grade(avg)

    print("\nStudent Results:")
    print(f"Name: {name}")
    print("Marks:")
    for subject, score in marks:
        print(f"  {subject}: {score}")
    print(f"Total: {total}")
    print(f"Average: {avg:.2f}")
    print(f"Grade: {grade}")