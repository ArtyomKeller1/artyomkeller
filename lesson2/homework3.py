seasons = {'Зима': (1, 2, 12),
           'Весна': (3, 4, 5),
           'Лето': (6, 7, 8),
           'Осень': (9, 10, 11)}

month = int(input())
for key in seasons.keys():
    if month in seasons[key]:
        print(key)