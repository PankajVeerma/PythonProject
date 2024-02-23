profit = 0
resourse = {
    "water":500,
    "milk":200,
    "coffee":100
    
}
menu = {
  "latte": {
      "ingradients":{
         "water":200,
         "milk":150,
         "coffee":20
         },
        "cost":150},
  "espresso": {
      "ingradients":{
         "water":50,
        #  "milk":150,
         "coffee":18
         },
        "cost":100},
  "cappuccion": {
      "ingradients":{
         "water":250,
         "milk":100,
         "coffee":24
         },
        "cost":200}

}
def check_resourses(order_ingradients):
    for item in order_ingradients:
        if order_ingradients[item]>resourse[item]:
            print(f"Sorry there is no enough{item}")
            return False
        return True
    
def process_coins():
    print("Please Insert coins:- ")
    total = 0
    coins_five = int(input("How many five's Coins Have you ?:"))
    coins_ten = int(input("How many ten's Coins Have you ?:"))
    coins_twenty = int(input("How many twenty's Coins Have you ?:"))
    total = coins_five + coins_ten  + coins_twenty 
    return total
def is_payment_successful(money_recieved , coffee_cost):
    if money_recieved>=coffee_cost:
        global profit
        profit==coffee_cost
        change = money_recieved - coffee_cost
        print(f"Here is your change Rs{change}")
        return True
    else:
        print("Sorry that is not enough money")
        return False

def make_coffee(coffee_name,coffee_ingradients):
    for item in coffee_ingradients:
        resourse[item] -= coffee_ingradients[item]
    print(f"Here is your ☕☕☕{coffee_name}.....Enjoy it")
  
        
is_on = True
while is_on:
    choice = input("What would you have to like?(latte/espresso/cappuccion): ")
    if choice=="off":
        is_on = False
    elif choice == "report":
        print(f"water is {resourse['water']}ml")
        print(f"milk is {resourse['milk']}ml")
        print(f"coffee is {resourse['coffee']}ml")
        print(f"money is Rs{(profit)}")
    else:
        coffee_type = menu[choice]
        print(coffee_type)
        check_resourses=(coffee_type['ingradients'])
        payment = process_coins()
        if is_payment_successful(payment,coffee_type['cost']):
            make_coffee(choice,coffee_type['ingradients'])
        