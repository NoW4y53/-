import json
#1
def display_product_info(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    for product in data["products"]:
        name = product["name"]
        price = product["price"]
        weight = product["weight"]
        available = "В наличии" if product["available"] else "Нет в наличии!"
        print(f"Название: {name}")
        print(f"Цена: {price}")
        print(f"Вес: {weight}")
        print(available)
        print()

path = "products.json"
#display_product_info(path)
#2
def add_product(path, name, price, weight, available):
    name = input("Введите название продукта: ")
    price = float(input("Введите цену продукта: "))
    weight = int(input("Введите вес продукта: "))
    available = input("Продукт в наличии? (да/нет): ").lower() == "да"
   
  with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    product = {
        "name": name,
        "price": price,
        "weight": weight,
        "available": available
    }
    data["products"].append(product)
    with open(json_file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    
    print("Обновленная информация о продуктах:")
    display_product_info(path)
#add_product_to_json(path, name, price, weight, available)

#3
def dictionary(input_file_path, output_file_path):
    russian_english_dict = {}

    with open(input_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            english_word, russian_translations = line.strip().split(" - ")
            russian_words = [word.strip() for word in russian_translations.split(",")]
            for russian_word in russian_words:
                russian_english_dict[russian_word] = english_word

    sorted_dict = dict(sorted(russian_english_dict.items()))

    with open(output_file_path, 'w', encoding='utf-8') as file:
        for russian_word, english_word in sorted_dict.items():
            file.write(f"{russian_word} - {english_word}\n")

input_file_path = "en-ru.txt"
output_file_path = "ru-en.txt"

#dictionary(input_file_path, output_file_path)
