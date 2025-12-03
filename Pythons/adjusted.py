marks = [78,92,36,64,89]
total = sum(marks)
print(f"Sum of marks: {total}")
adjusted = [2,2,5,10,2]
adjmar = []
for i in range(len(marks)):
    adjmar.append(marks[i]+adjusted[i])
print(adjmar)
subjects = ["Maths","Science","English","history","UHV"]

for i in range(len(subjects)):
    print(f"Subject{subjects[i]} : {adjmar[i]}")