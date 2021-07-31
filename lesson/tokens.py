import time
import requests
import json

url = "https://playground.learnqa.ru/ajax/api/longtime_job"

response = requests.get(url)
obj = json.loads(response.text)
token = obj["token"]
sec = obj["seconds"]
print(f"1 - задача создана c token={token}, будет выполнена через {sec} сек")

payload = {"token": token}
response = requests.get(url, params=payload)
obj = json.loads(response.text)

if "status" in obj:
    status = obj["status"]
    if status == 'Job is NOT ready':
        print(f"2 - {status} => проверка выполнена успешно, задача ещё не готова")
    else:
        print(f"2 - {status} => проверка выполнена не успешно: задача готова / вернулся неизвестный статус")
else:
    print("2 - передан некорректный токен")

time.sleep(sec)
print(f"3 - выполняю проверку задачи по прошествии {sec} сек")
payload = {"token": token}
response = requests.get(url, params=payload)
obj = json.loads(response.text)
if "status" in obj:
    status = obj["status"]
    if status == 'Job is ready':
        print(f"2 - {status} => проверка выполнена успешно, задача готова")
    else:
        print(f"2 - {status} => проверка выполнена не успешно: задача не готова / вернулся неизвестный статус")
else:
    print("2 - передан некорректный токен")


