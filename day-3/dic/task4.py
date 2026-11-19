words = ["apple", "ant", "banana", "bat", "cat", "carrot"]

grouped = {}

for word in words:
    first = word[0]
    grouped.setdefault(first, []).append(word)

print(grouped)