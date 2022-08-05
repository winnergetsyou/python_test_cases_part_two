class Test_cases():    
    @classmethod
    def setup_class(cls):
        print('\nexecuting the setup_classes\n')
    @classmethod
    def teardown_class(cls):
        print('\ncompleted all the class_test_cases\n')
        
    def test_function_one(self):
        assert True
    def test_function_two(self):
        assert True

def setup_function():
    print('\nfunction test started ')
def teardown_function():
    print('\nfunction test completed')
    
def test_new_one():
    assert True
def test_new_two():
    assert True
    
def setup_module():
    print ('just beginning')
def teardown_module():
    print ('ending')