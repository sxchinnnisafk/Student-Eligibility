subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))
subject4 = float(input("Enter marks for subject 4: "))
subject5 = float(input("Enter marks for subject 5: "))

average = (subject1 + subject2 + subject3 + subject4 + subject5) / 5

if subject1 >= 40 and subject2 >= 40 and subject3 >= 40 and subject4 >= 40 and subject5 >= 40:
	if average >= 90:
		grade = "A"
	elif average >= 80:
		grade = "B"
	elif average >= 70:
		grade = "C"
	elif average >= 60:
		grade = "D"
	else:
		grade = "F"
	print("Student is PASSED")
	print(f"Average: {average:.2f}")
	print(f"Grade: {grade}")
else:
	print("Student is FAILED")
	print("Grade: F")