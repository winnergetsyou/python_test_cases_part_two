#production code :
def production_code_one(number):
    divide_three = number%3
    divide_five = number % 5
    print(divide_three)
    
    if divide_five==0 and divide_three==0:
        print(divide_three)
        print(divide_five)
        return "Fizzbuzz"
    elif divide_three == 0:
        return "Fizz"
    elif divide_five == 0:
        return "buzz"
    else:
        return number