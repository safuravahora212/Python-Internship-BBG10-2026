call_count = 0

def track_calls():
    global call_count
    call_count += 1

# Call the function 4 times
for _ in range(4):
    track_calls()

print(f"Total calls: {call_count}")
