import one as h



def opt(value,expected_value):
    function_return=h.production_code_one(value)
    assert function_return == expected_value

# test_cases
def test_case_one():
    opt(1,1)

def test_case_two():
    number = 2
    action = h.production_code_one(number)
    assert action == 2
    
def test_case_three():
    number = 3 # setup
    action = h.production_code_one(number) # action --> call the production code
    assert action == "Fizz"
    
def test_case_four():
    number = 5 # setup
    action = h.production_code_one(number)
    print(action)
    assert action == "buzz"

def test_case_five():
    opt(6,"Fizz")
    
def test_case_six():
    opt(10,"buzz")
def test_case_seven():
    opt(15,"Fizzbuzz")