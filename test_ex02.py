from ex02.dot_product import dot_product

class Test_Ex03:
    def testcase_1(self):
        assert dot_product([1, 2, 3], [4, 5, 6]) == 32
    
    def testcase_2(self):
        assert dot_product([1, 2], [3, 4, 5]) == 0

    def testcase_3(self):
        assert dot_product([-1, 2], [7, 3]) == -1

    def testcase_4(self):
        assert dot_product([-1, 1, -1, 1, -1], [2, 5, 4, 7, 10]) == -4