import requests
import pytest


class TestUserAgent:
    data = [
        ({"user-agent": "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
          "expected_platform": "Mobile",
          "expected_browser": "No",
          "expected_device": "Android"
          }),
        ({"user-agent": "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1",
          "expected_platform": "Mobile",
          "expected_browser": "Chrome",
          "expected_device": "iOS"
          }),
        ({"user-agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
          "expected_platform": "Googlebot",
          "expected_browser": "Unknown",
          "expected_device": "Unknown"
          }),
        ({"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0"
          "Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0",
          "expected_platform": "Web",
          "expected_browser": "Chrome",
          "expected_device": "No"
          }),
        ({"user-agent": "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
          "expected_platform": "Mobile",
          "expected_browser": "No",
          "expected_device": "iPhone"
          })
    ]

    @pytest.mark.parametrize('data', data)
    def test_user_agent(self, data):
        user_agent = data["user-agent"]
        expected_platform = data["expected_platform"]
        expected_browser = data["expected_browser"]
        expected_device = data ["expected_device"]

        response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check", headers={"User-Agent": user_agent})

        response_dict = response.json()

        received_platform = response_dict['platform']
        received_browser = response_dict['browser']
        received_device = response_dict['browser']

        assert expected_platform == received_platform, f"Значение платформы {received_platform} отличается от ожидаемого {expected_platform}"
        assert expected_browser == received_browser, f"Значение браузера {received_browser} отличается от ожидаемого {expected_browser}"
        assert expected_device == received_device, f"Значение девайса {received_device} отличается от ожидаемого {expected_device}"
