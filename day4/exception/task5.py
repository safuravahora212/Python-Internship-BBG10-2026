while True:
    try:
        num = int(input("Enter a number between 1 and 10: "))
        
        if num < 1 or num > 10:
            raise ValueError("Number out of range!")

        print("Valid number:", num)
        break 

    except ValueError as e:
        print("Invalid! Please try again.", e)