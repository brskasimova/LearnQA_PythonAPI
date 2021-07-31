import requests


class TestHeader:

    def test_header(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        print(response.headers)
        received_value = response.headers.get('x-secret-homework-header')
        expected_value = 'Some secret value'

        assert received_value == expected_value, f"Значение заголовка {received_value} отличается от ожидаемого {expected_value}"
