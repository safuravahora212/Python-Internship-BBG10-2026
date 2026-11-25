def build_invoice(customer_name, *args, **kwargs):
    total = sum(args)
    print("Customer:", customer_name)
    print("Total:", total)
    for key, value in kwargs.items():
        print(f"{key}: {value}")


build_invoice("Rahul", 100, 200, 300, discount=50, tax=18)                  