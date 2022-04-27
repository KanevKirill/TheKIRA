#  Формирование вывода

file_name = 'recept.txt'


def file_worker():
    cook_book = {}
    with open('recept.txt', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if '|' not in line and not line.isdigit() and len(line) > 1:
                dish_name = line
                cook_book[dish_name] = []
                num = int(file.readline().strip())
                while num > 0:
                    ingr_info = file.readline().strip().split('|')
                    if len(ingr_info) > 0:
                        cook_book[dish_name].append({'ingredient': ingr_info[0],
                                                     'quantity': ingr_info[1],
                                                     'units': ingr_info[2]})
                        num -= 1
    return cook_book


print(file_worker())

#  Функция рассчета кол-ва ингредиентов

cook_book = file_worker()


def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient']
                if ingredient_name not in result.keys():
                    result[ingredient_name] = {
                        'units': ingredient['units'],
                        'quantity': int(ingredient['quantity']) * person_count
                    }
                else:
                    result[ingredient_name]['quantity'] += int(ingredient['quantity']) * person_count

    return result


result1 = get_shop_list_by_dishes(['Омлет'], 2)
result2 = get_shop_list_by_dishes(['Омлет', 'Омлет'], 1)
result3 = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 1)
print(result1)
print(result2)
print(result3)