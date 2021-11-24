import json

with open('D:\pokemon_full.json') as file:
    text = file.read()
    print('Всего символов в тексте:', len(text))

    k = 0    #k-число символов, не учитывая пробелы и знаки перпинания.
    for i in text:
        if i.isalnum():
            k += 1
    print('Всего символов в тексте, не учитывая пробелы и знаки препинания:', k)

    list = json.loads(text)
    desc = 0
    name_of_pokemon = ''
    for item in list:
        description = item['description']
        if len(description) > desc:
            desc = len(description)
            name_of_pokemon = item['name']
    print('Наиболее длинное описание имеет покемон', name_of_pokemon)

    words = 0
    ability = ''
    for item in list:
        abilities = item['abilities']
        for i in abilities:
            if len(i.split()) > words:
                words = len(i.split())
                ability = i
    print('Больше всего слов содержит умение', ability)

    #Задание на защиту
    all_speeds = 0
    speeds = []
    speed = 0
    counter_of_pokemons = 0
    for item in list:
        speed += item['stats']['speed']
        counter_of_pokemons += 1
    m = speed / counter_of_pokemons
    for item in list:
        speeds.append(item['stats']['speed'])
    for i in speeds:
        all_speeds += (i - m)**2
    s = (all_speeds / m)**0.5 
    for item in list:
        if (item['stats']['speed'] > m + s) or (item['stats']['speed'] < m - s):
            print('Покемон с нетипичной скоростью: ' + item['name'])
