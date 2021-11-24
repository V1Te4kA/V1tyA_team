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
