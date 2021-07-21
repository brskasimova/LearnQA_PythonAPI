import requests
from random import choice

url = "https://playground.learnqa.ru/api/compare_query_type"

response1 = requests.get(url)
response2 = requests.post(url)
response3 = requests.put(url)
response4 = requests.delete(url)
print(f"1 - GET /api/compare_query_type без параметра method: статус код {response1.status_code}, ответ {response1.text}")
print(f"    POST /api/compare_query_type без параметра method: статус код {response2.status_code}, ответ {response2.text}")
print(f"    PUT /api/compare_query_type без параметра method: статус код {response3.status_code}, ответ {response3.text}")
print(f"    DELETE /api/compare_query_type без параметра method: статус код {response4.status_code}, ответ {response4.text}")

response5 = requests.patch(url)
print(f"2 - PATCH /api/compare_query_type: статус код: {response5.status_code}, ответ: {response5.text}")

payload6 = {"method": "GET"}
response6 = requests.get(url, params=payload6)
payload7 = {"method": "POST"}
response7 = requests.post(url, data=payload7)
payload8 = {"method": "PUT"}
response8 = requests.put(url, data=payload8)
payload9 = {"method": "DELETE"}
response9 = requests.delete(url, data=payload9)
print(f"3 - GET /api/compare_query_type c параметром method=GET: статус код {response6.status_code}, ответ {response6.text}")
print(f"    POST /api/compare_query_type c параметром method='POST': статус код {response7.status_code}, ответ {response7.text}")
print(f"    PUT /api/compare_query_type c параметром method='PUT': статус код {response8.status_code}, ответ {response8.text}")
print(f"    DELETE /api/compare_query_type c параметром method='DELETE': статус код {response9.status_code}, ответ {response9.text}")

print(f"4 -")
list_methods = ["GET", "POST", "PUT", "DELETE"]
result = []
for i in list_methods:
    payload = {"method": i}
    response10 = requests.get(url, params=payload)
    print(f"    GET с параметром method={i}: статус код {response10.status_code}, ответ {response10.text}")
    response11 = requests.post(url, data=payload)
    print(f"    POST с параметром method={i}: статус код {response11.status_code}, ответ {response11.text}")
    response12 = requests.put(url, data=payload)
    print(f"    PUT с параметром method={i}: статус код {response12.status_code}, ответ {response12.text}")
    response13 = requests.delete(url, data=payload)
    print(f"    DELETE с параметром method={i}: статус код {response13.status_code}, ответ {response13.text}")
