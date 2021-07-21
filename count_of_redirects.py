import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
history = response.history
count = len(history)

print(history)
print(f"Последний location {response.url}")
print(f"Количество редиректов {count}")