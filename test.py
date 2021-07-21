import requests
from random import choice

url = "https://playground.learnqa.ru/api/compare_query_type"
list_methods = ["GET", "POST", "PUT", "DELETE"]
method = choice(list_methods)
print(method)


