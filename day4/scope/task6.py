def make_validator(min_value):
    def check(number):
        return number >= min_value
    return check

check_18 = make_validator(18)
check_60 = make_validator(60)

print(check_18(20))  
print(check_18(10))  

print(check_60(70))  
print(check_60(50))  