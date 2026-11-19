employees = {"Aisha": 50000, "Rahul": 75000, "Sara": 62000, "Aman": 90000, "Priya": 48000}

# salary pramane descending ma sort
sorted_emp = sorted(employees.items(), key=lambda x: x[1], reverse=True)

# top 3 j print karo
for name, salary in sorted_emp[:3]:
    print(name, salary)