print("-------------------------")
print("Welcome to Our Cafe")
print("-------------------------")

menu = {
    'pizza' : 50,
    'salad' : 30,
    'burger' : 100,
    'popcorn' : 100
}

print('pizza-50\nsalad-30\nburger-100\npop corn-100')
order_item= input('Enter your item:')

order_total = 0

if order_item in menu:
    order_total += menu[order_item]
    order = input("Anything Else (yes/no):")

    if order == 'yes':
        order_item2 = input('Enter item please:')

        if order_item2 in menu:
            order_total += menu[order_item2]
            print(f'your order value:{order_total}')

    else:
        print(f'your order value:\\t{order_total}')
        
else:
    print('No item with that name sorry:)')
