print('Hello, welcome to NetworkChuck.coffee!!!!!!')

name = input('What is your Name ?\n')
print('Hello '+ name + ',thank you so much for coming in today.')

menu= 'espresso, latte, black coffee , cappuccino, nescafe'

print(name + ' What would you like from our menu today ? Here is what we are serving\n '+ menu)
order = input()

if order == 'nescafe':
    price = 10
elif order == 'latte':
    whipped = input('Would you like whipped cream ?\n')
    if whipped == 'Yes':
        price = 17
    else:
        price = 15
elif order == 'black coffee':
    price = 5
elif order == 'espresso':
    price = 15
elif order == 'capuccino':
    price = 20
else:
    print("Sorry we don't have that on our Menu.")
    exit()


ordernumber = input('How many coffees would you like?\n')

total = price * int(ordernumber)
print(total)

print('Your total is $' +str(total))

print('Thank you ' + name + ', Your '+ ordernumber + ' ' + order + ' will be served in a few minutes.')