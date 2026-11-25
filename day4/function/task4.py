usernames = ["ram", "shyam123", "priya", "rahul_07", "a", "anita123"]
long_names = list(filter(lambda name: len(name) >= 6, usernames))
print(long_names)