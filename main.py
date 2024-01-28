import requests

movie_ids = [
    238,
    680,
    550,
    185,
    641,
    515042,
    152532,
    120467,
    872585,
    906126,
    840430
]

datas = []

for movie_id in movie_ids:
    URL = f"https://nomad-movies.nomadcoders.workers.dev/movies/{movie_id}"
    response = requests.get(URL)
    data = response.json()
    id_data = {}
    id_data["title"] = data["title"]
    id_data["overview"] = data["overview"]
    id_data["vote_average"] = data["vote_average"]
    datas.append(id_data)
print(datas)
