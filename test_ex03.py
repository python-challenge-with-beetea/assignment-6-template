from ex03.is_palindrome import is_palindrome

class Test_Ex03:
    def testcase_1(self):
        assert is_palindrome("토마토") == True
    
    def testcase_2(self):
        assert is_palindrome("파이썬") == False

    def testcase_3(self):
        assert is_palindrome("tomok") == False

    def testcase_4(self):
        assert is_palindrome("러시아아시러") == True

    def testcase_5(self):
        assert is_palindrome("level") == True