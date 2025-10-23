# Build a program that takes a student’s marks in multiple subjects, calculates their average,
# and gives feedback and a grade based on performance

student_name = input("Enter your your full name: ")
print("\nEnter Marks of the following subjects:\n")

math = int(input("1. Math: "))
english = int(input("2. English: "))
science = int(input("3. Science: "))
history = int(input("4. History: "))
computer = int(input("5. Computer: "))

# calculate the average mark of all subjects

total_marks = math + english + science + history + computer
average_mark = total_marks / 5

if average_mark >= 80:
    grade = "A"
    msg = "Excellent work!"
elif average_mark >= 70:
    grade = "B"
    msg = "Good job!"
elif average_mark >= 60:
    grade = "c"
    msg = "You passed, but can improve!"
elif average_mark >=  50:
    grade = "D"
    msg = "Need improvement!"
else:
    grade = "F"
    msg = "Failed!"

print(f"\n---------------{student_name}'s report form---------------\n")
print("Subject:\t\t\tMark(%):\n")
print(f"Math:\t\t\t\t{math}\n")
print(f"English:\t\t\t{english}\n")
print(f"Science:\t\t\t{science}\n")
print(f"History:\t\t\t{history}\n")
print(f"Computer:\t\t\t{computer}")
print("--------------------------------------------------------")
print(f"Total marks:\t\t\t{total_marks}\n\n")
print("--------------------------------------------------------")
print(f"Average mark:\t\t\t{average_mark}%\n")
print(f"Grade:\t\t\t\t{grade}\n")
print(f"\t\t{msg}")
print("--------------------------------------------------------\n")
