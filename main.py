import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Dados recebidos da API:")
    print(data)
else:
    print("Erro ao acessar API:", response.status_code)
