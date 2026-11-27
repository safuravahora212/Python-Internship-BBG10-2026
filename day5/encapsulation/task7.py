import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        print(f"Time taken: {end - self.start:.4f} seconds")

# Test - 1 million loop
with Timer():
    total = 0
    for i in range(1000000):
        total += i
    print(total)