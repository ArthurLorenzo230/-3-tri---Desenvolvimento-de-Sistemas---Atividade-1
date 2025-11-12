import requests

API_KEY = 'SUA_API_KEY'  # Substitua pela sua chave real
query = 'playstation'

url = 'https://www.googleapis.com/youtube/v3/search'
params = {
    'part': 'snippet',
    'q': query,
    'type': 'video',
    'maxResults': 5,
    'key': API_KEY
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    for item in data['items']:
        title = item['snippet']['title']
        video_id = item['id']['videoId']
        print(f"{title}: https://www.youtube.com/watch?v={video_id}")
else:
    print(f"Erro: {response.status_code}")
