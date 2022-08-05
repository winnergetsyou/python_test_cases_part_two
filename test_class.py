class Test_cases():    
    @classmethod
    def setup_class(cls):
        print('executing the setup_classes\n')
    @classmethod
    def teardown_class(cls):
        print('\ncompleted all the class_test_cases\n')
        
    def test_function_one(self):
        assert True
    def test_function_two(self):
        assert True