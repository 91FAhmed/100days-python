from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

CoffeeMaker = CoffeeMaker()
MoneyMachine = MoneyMachine()

action = input("Enter a expresso/latte/etc:").lower()

if(action == 'report'): #instanciate 
   print(MoneyMachine.report())

Menus = Menu()
drink =  Menus.find_drink(action)

if(drink != "None"):
  
  
  if(MoneyMachine.make_payment(drink.cost) == True):
     if(CoffeeMaker.is_resource_sufficient(drink) == True):
      CoffeeMaker.make_coffee(drink)
   
   