class TestExample:
    def test_check_math(self):
        a = 5
        b = 9
        expected_some = 14
        assert a + b == expected_some, f"Some of variables a and b is not equal to {expected_some}"

    def test_check_math2(self):
        a = 5
        b = 11
        expected_some = 14
        assert a+b == expected_some, f"Some of variables a and b is not equal to {expected_some}"
