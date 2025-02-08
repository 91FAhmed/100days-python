import resources_object

coin_base = {
    "quaters":0.25,
    "nickel":0.05,
    "dime":0.10,
    "penny":0.01,
}


money  = float(0)


def calc_cost(item):
 print("please enter coins:")
 quaters = float(input("please enter quaters:"))
 dimes = float(input("please enter dime:"))
 nickles = float(input("please enter nickle:"))
 penny = float(input("please enter penny:"))
 
 return (coin_base["quaters"] * quaters) + (coin_base['dime'] * dimes) + (coin_base["nickel"] * nickles) + (coin_base["penny"] * penny)


    

while True:
    user_selection =  input("what would you like? (espresso/latte/cappuccino): ").lower()
    if(user_selection == 'report'):
        print(f"water:{resources_object.resources['water']}ml\nmilk:{resources_object.resources['milk']}ml\ncoffee:{resources_object.resources['coffee']}gm")
    elif(user_selection == 'espresso' or user_selection == 'latte' or user_selection == 'cappuccino' ):
       ans = calc_cost(item=user_selection)
       print(ans)


