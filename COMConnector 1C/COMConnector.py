import requests

url = "http://адрес_1с/ваш_веб_сервис/endpoint"
auth = ('Володин С.В.', 'Master023')

response = requests.get(url, auth=auth)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Ошибка доступа:", response.status_code)

