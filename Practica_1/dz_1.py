# 1 задача

products = {"Cake": ['Ingredients: sugar, flour, vanilla, milk.', 8.5, 1000], # 1 аргумент - состав, 2 - цена за 100гр, 2 - кол-во в граммах
            "Pie": ['Ingredients: flour, sugar, eggs, butter, milk.', 5.5, 500],
            "Muffin": ['Ingredients: flour, sour cream, eggs, butter.', 4.0, 700],
            "Cookie": ['Ingredients: flour, sugar, eggs, butter, vanilla.', 3.5 , 800]}

for key,value in products.items(): # вывод
    print(key, '-', value[0], 'Цена за 100гр:', value[1], 'Количество: ', value[2])

while True:
        product = input("Если вас интересует состав продукции, введите f. Если цена, введите r. Если количество, введите s. Для перехода к покупкам введите a: ")
        if product=='f':
            product = input("Введите продукцию, состав которой вас интересует: ")
            print(products[product][0])
        elif product=='r':
            product = input("Введите продукцию, цена которой вас интересует: ")
            print(products[product][1])
        elif product=='s':
            product = input("Введите продукцию, количество которой вас интересует: ")
            print(products[product][2])
        elif product=='a' or product not in products:
            break

cost = 0
while True:
    product = input("Введите товар, который хотите купить или введите n для выхода: ")
    if product == 'n' or product not in products:
        break
    qty = int(input("Сколько Вы хотите купить? "))
    if qty > products[product][2]:
        print("У нас столько нет, выберите другое количество или товар: ")
        continue
    cost = cost + (qty * products[product][1])
    products[product][2] -= qty
print(f"Вам надо заплатить {cost} р.")


