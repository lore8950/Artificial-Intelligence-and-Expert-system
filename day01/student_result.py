#Take student name and marks, print pass or fail

student_name = input("Enter student's name: ")
marks = float(input(f"Enter {student_name}'s marks: "))

passing_mark = 50 # Assuming 50 as the passing mark

if marks >= passing_mark:
    print(f"{student_name} has passed!")
else:
    print(f"{student_name} has failed.")
