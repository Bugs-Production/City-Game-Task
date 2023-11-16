# Игра в города
import random as rd


# функция для чистки слов
def normalize_city_name(name):
    return name.strip().lower().replace('ё', 'е')


# функция для передачи предпоследнего символа
def last_letter(word):
    if word[-1] == 'ь' or word[-1] == 'й':
        return word[-2]
    else:
        return word[-1]


# создаем пустой список для будущих городов
words_city = []

# достаем города из текстового файла
with open('citylist.txt', 'r', encoding='utf-8') as item:
    for i in item:
        words_city.append(normalize_city_name(i))

# создаем переменную для случайного города, с рандомным индексом
random_city = words_city[rd.randint(0, len(words_city))]

while True:
    print(f'Компьютер назвал город {random_city.capitalize()}')
    last_char_pk = last_letter(random_city)
    print(f'Назови город на букву {last_char_pk.capitalize()}')
    words_city.remove(random_city)

    user_city = input(f'Твой ответ - ').lower()
    last_char_user = last_letter(user_city)

    if last_char_pk == user_city[0] and user_city in words_city:
        words_city.remove(user_city)
        for city in words_city:
            if city[0] == last_char_user:
                random_city = city
                break
    else:
        print('Данного города нет в списке, либо уже был использован')
        break
