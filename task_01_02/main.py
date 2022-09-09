from pprint import pprint

cook_book = {}

with open("text.txt", encoding="utf-8") as file:
    for line in file:
        name_dish = line.strip()
        dish_count = file.readline().strip()
        ingridients = []
        for item in range(int(dish_count)):
            items = file.readline().strip().split(" | ")
            ingridients.append({"ingredient_name": items[0], "quantity": items[1], "measure": items[2]})
        cook_book[name_dish] = ingridients
        file.readline()

pprint(f"cook_book = {cook_book}")

def get_shop_list_by_dishes(dishes, person_count):
    total_ingredients = {}
    name_list = []
    measure_list = []
    quantity_list = []

    for item in dishes:
        if item in cook_book:
            items = cook_book[item]
            for item in items:
                name_list.append(item["ingredient_name"])
                measure_list.append(item['measure'])
                quantity_list.append(item['quantity'])

    for item in range(len(name_list)):
        if name_list[item] not in total_ingredients:
            total_ingredients[name_list[item]] = {'measure': measure_list[item],
                                                  'quantity': person_count * int(quantity_list[item])}
        else:
            for i in total_ingredients[name_list[item]]:
                if i == "quantity":
                    total_ingredients[name_list[item]][i] += person_count * int(quantity_list[item])

    pprint(total_ingredients)


get_shop_list_by_dishes(["Омлет", "Омлет", "Утка по-пекински"], 2)