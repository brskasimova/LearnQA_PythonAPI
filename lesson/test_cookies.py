import requests


class TestCookies:

    def test_cookies(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        cookies = dict(response.cookies)
        print(cookies)
        received_value = cookies.get("HomeWork")
        expected_value = 'hw_value'

        assert received_value == expected_value, f"Значение куки {received_value} отличается от ожидаемого {expected_value}"
