from ex04.strange_cmp import strange_cmp

class Test_Ex04:
    def testcase_1(self):
        assert strange_cmp(123, 321) == "Same"
    
    def testcase_2(self):
        assert strange_cmp(222, 321) == "Left"

    def testcase_3(self):
        assert strange_cmp(911, 537) == "Right"

    def testcase_4(self):
        assert strange_cmp(1111, 999) == "Left"

    def testcase_5(self):
        assert strange_cmp(221, 222) == "Right"