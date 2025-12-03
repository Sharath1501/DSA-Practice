def grades(mark):
    if 91 <= mark <= 100:
        return "Grade S"
    elif 81 <= mark <= 90:
        return "Grade A"
    elif 71 <= mark <= 80:
        return "Grade B"
    elif 61 <= mark <= 70:
        return "Grade C"
    elif 51 <= mark <= 60:
        return "Grade D"
    elif 41 <= mark <= 50:
        return "Grade E"
    elif 0 <= mark <= 40:
        return "Grade F"
    else:
        return "Invalid Mark"

for i in range(1, 5):
    mark = int(input(f"Enter the mark for subject {i}: "))
    print(f"Grade of subject {i} is: {grades(mark)}")
