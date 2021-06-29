import requests as r
cityname= str(input())
apikey = "97b6185409cdebf023b691da4653256b"
url = f"http://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={apikey}"
data = r.get(url)
data1 = data.json()
print(f"В городе {cityname} {data1['main']['temp']} градусов по Кельвину")