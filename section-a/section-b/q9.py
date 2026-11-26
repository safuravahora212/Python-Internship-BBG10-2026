marks = [80, 75, 90, 65, 70]

total = 0

for mark in marks:
    total += mark

max_marks=len(marks)*100
percentage = total / 500 * 100

if percentage >= 35:
    result = "PASS"
else:
    result = "FAIL"

print("Total:", total)
print("Percentage:", percentage)
print("Result:", result)