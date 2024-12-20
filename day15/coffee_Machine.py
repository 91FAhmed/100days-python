import resources_object

coin_base = {
    "quaters":0.25,
    "nickel":0.05,
    "dime":0.10,
    "penny":0.01,
}


money  = float(0)


def calc_cost(item,money):
 print("please enter coins:")
 quaters = float(input("please enter quaters:"))
 dimes = float(input("please enter dime:"))
 nickles = float(input("please enter nickle:"))
 penny = float(input("please enter penny:"))
 
 total = round((coin_base["quaters"] * quaters) + (coin_base['dime'] * dimes) + (coin_base["nickel"] * nickles) + (coin_base["penny"] * penny),2)
 if(total < resources_object.MENU[item]['cost']):
    print("The amount is less")
 else:
   print(f"Here is your change {total - resources_object.MENU[item]['cost']}$ Enjoy ☕️") 
#    for items in range(0,len(resources_object.MENU[item]['ingredients'])):
#       resources_object.resources[items] -= resources_object.MENU[item]['ingredients'][items]
   for resource in resources_object.MENU[item]['ingredients']:
      resources_object.resources[resource] -= resources_object.MENU[item]['ingredients'][resource]
   print(resources_object.resources)
   return resources_object.MENU[item]['cost']

def check_resources(item):
    for resource in resources_object.MENU[item]['ingredients']:
       if(resources_object.resources[resource] < resources_object.MENU[item]['ingredients'][resource]):
          
          return False
   
    

while True:
    user_selection =  input("what would you like? (espresso/latte/cappuccino): ").lower()
    if(user_selection == 'report'):
        print(f"water:{resources_object.resources['water']}ml\nmilk:{resources_object.resources['milk']}ml\ncoffee:{resources_object.resources['coffee']}gm\nmoney:{money}$")
    elif(user_selection == 'espresso' or user_selection == 'latte' or user_selection == 'cappuccino' ):
       if(check_resources(item=user_selection) == False):
          print(" resorces are less please refil")
       else:
        ans = calc_cost(item=user_selection,money=money)
        money += ans


