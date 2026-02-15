menu = dict({'Tea':20, 
            'coffee':40,
            'lassi':35,
            'Salad':40,
            "Pohe":25,
            'Masala Dosa':35,
            'Misal':60,
            "Pavbhaji":60,
            'Plain Rice':30,
            'Pulav':40,
            'Bhaji-poli Thali':80
            })

print("Welcome to our Homemade Python Restaurant")
#menu
print("Our Menu is as follows:")
for i in menu:
    print(i,'=', menu[i])

ordered_items = 0
 

def order():
    global ordered_items
    item = input('Enter your first item according to menu:')
    ordered_items += menu[item]
flag = 1
def question():
    global flag, ordered_items
    Q1 = input('Do you want to order more items?(yes/no)')
    if Q1=='yes':
        item =input('Enter your next item according to our menu:')
        ordered_items += menu[item]
        flag += 1
        question()
    else:
        print(f"Total items are {flag}")
        print(f"Total amount {ordered_items} which you have to pay for your order.")
order()
question()

print('Thank you for visiting our restarunt')

Q2 = input("Did you like our service?(yes/no)")
if Q2=='yes':
    print('Thank you for your feedback')
else:
    input('Give your suggestion....')
    print('Thank you for your suggestions. We will try to upgrade our services as per your suggestion')
    pass

print('Plz, visit again !')
