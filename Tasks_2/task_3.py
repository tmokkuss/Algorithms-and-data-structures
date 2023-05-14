def group_cities_by_population(cities):
    data = {}

    for item in cities:
        city = item[0]
        population = item[2]
        interval = population // 100000 * 100
        if interval in data:
            data[interval].append(city)
        else:
            data[interval] = [city]

    sorted_intervals = sorted(data.keys())

    for interval in sorted_intervals:
        cities = sorted(data[interval])
        print(f"{interval} - {interval + 100}: {', '.join(cities)}")


cities = [
    ["Братислава", "Словакия", 625167],
    ["Брюссель", "Бельгия", 1154635],
    ["Будапешт", "Венгрия", 1757618],
    ["Белград", "Сербия", 1233796],
    ["Прага", "Чехия", 1267449],
    ["София", "Болгария", 1286383],
    ["Тбилиси", "Грузия", 1118035]
]

group_cities_by_population(cities)
