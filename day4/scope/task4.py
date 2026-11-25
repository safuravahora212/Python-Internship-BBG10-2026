def outer():
    status = "pending"

    def inner():
        nonlocal status
        status = "completed"

    inner()
    print("Final status:", status)

outer()
