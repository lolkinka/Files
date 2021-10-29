from pprint import pprint
import os


with open('recipe.txt', encoding='utf-8') as file:
    cook_book = dict()
    for line in file:
        food = line.strip()
        counter = int(file.readline())

        list = []
        for items in range(counter):
            ingrideint_name, quantity, measure = file.readline().split("|")
            list.append(
                {'ingridient_name': ingrideint_name,
                 'quantity': quantity,
                 'measure' : measure}
            )
        cook_book[food] = list
        file.readline()

pprint(cook_book)



def get_shop_list_by_dishes(dishes, person_count):
    empty_dict = dict()
    for food in dishes:
        if food in cook_book.keys():
            for dictionary in (cook_book[food]):
                empty_dict = { dictionary['ingridient_name']:
                    {'quantity' : (int(dictionary['quantity']) * person_count),
                    'measure' : (dictionary['measure'])}
                }
                pprint(empty_dict)
        else:
            pprint('Такого блюда нет')


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'],2)

def union():
    path = 'C:\Python\python разработчик\Txts'
    dict = {}
    list_kolichestva = []
    for filename in os.listdir(path):
        counter = 0
        with open(os.path.join(path,filename), 'r', encoding='utf-8') as f:
            text = f.read()
            with open(os.path.join(path, filename), 'r', encoding='utf-8') as f:
                for line in f:
                    counter +=1
                list_kolichestva.append(counter)
                dict[filename] = counter , text
    list_kolichestva = sorted(list_kolichestva)
    new_dict = {}
    for el in list_kolichestva:
        for keys,values in dict.items():
            if values[0] == el:
                new_dict[keys] = values
    with open('union.txt', 'w',encoding='utf-8') as file:
        for keys, values in new_dict.items():
            file.write(f"{keys}\n")
            file.write(f"{str(values[0])}\n")
            file.write(f"{values[1]}\n")
            file.write(f"\n")
union()









