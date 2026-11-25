mode = "global"  # Global

def outer():
    mode = "outer"  # Enclosing

    def inner():
        mode = "inner"  # Local
        print("Inside inner:", mode)

    inner()
    print("Inside outer:", mode)

outer()
print("Outside:", mode)