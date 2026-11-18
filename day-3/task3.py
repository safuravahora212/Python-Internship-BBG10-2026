numbers = [20,30,40,40,50,50,60,65,70,100]

unique_numbers = []

for n in numbers:
    if n not in unique_numbers:
        unique_numbers.append(n)

print("Original List:", numbers)
print("Without Duplicates:", unique_numbers)