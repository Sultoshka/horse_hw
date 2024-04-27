shelf_products = {'продукты в полке':{'': 30}}

shopping_cart = []

consulting = input(f'какой продукт вы хотите добавить в: ')

product_name = input(f'название продукта каторый вы хотите добавить в: ')

product_count = input(f'сколько продуктов вы хотите добавить в: ')

shelf_products['продукты в полке'][product_name] -= 3

shopping_cart[product_name] = ''

print(shopping_cart)

print(shelf_products)

i_will_buy = input()

print(shopping_cart)

shopping_cart.remove = input()
