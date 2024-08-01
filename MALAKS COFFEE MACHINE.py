import random
# available initial resources:
def initial_coffee_resources():
    water = random.randint(800, 1000)
    coffee = random.randint(400, 800)
    milk = random.randint(200, 400)
    money = 0
    return water, coffee, milk, money
water, coffee, milk, money = initial_coffee_resources()
print("malaks coffee machine")
print("Current Coffee Machine Resources:")
print(f"Water: {water} ml")
print(f"Coffee Beans: {coffee} mg")
print(f"Milk: {milk} ml")
print(f"Money: {money}JD")
print("Espresso = 2JD, Latte = 3JD, Cappiccino = 3.5JD")
def check_resources(water, coffee, milk, required_water, required_coffee, required_milk):
    return (
        water >= required_water
        and coffee >= required_coffee
        and milk >= required_milk)
 
Espresso = {"Water": 80, "Coffee": 200, "Milk": 0, "cost": 2}
Latte = {"Water": 100, "Coffee": 100, "Milk": 100, "cost": 3}
Cappiccino = {"Water": 100, "Coffee": 75, "Milk": 150, "cost": 3.5}
deposit = [0]
money = sum(deposit)
print(input("What would you like?"))
if Espresso : 

    print ("checking resources!!")
    def check_resources(water, coffee, milk, required_water, required_coffee, required_milk):
     return (
        water >= required_water
        and coffee >= required_coffee
        and milk >= required_milk )
    print("your coffee will be made soon!")
money_message = f"That would be: JD{Espresso['cost']:.2f}"
    #realized need to find a way to check if i have enough resources lollololols
while True:
    amount_paid = float(input("Pay ahead: JD"))
    
    if amount_paid == 2.00:
        print("Thank you! Your remainder is 0")
        deposit.append(amount_paid)
        break 
    elif amount_paid > 2.00:
        remainder = amount_paid - 2.00
        print(f"Thank you! Your remainder is JD{remainder:.2f}")
        deposit.append(2.00)
        break 
    else:
        print(f"Insufficient payment. Please pay JD{Espresso['cost']:.2f}")
while True :
   choice = (input("would you like to order something else? (yes/no)"))
   if choice != 'yes' : 
       print(input("write off to exit!!"))
       break

   elif choice == 'yes' : 
       print(input("what would you like?"))
       


       


       
       

     
   
   

    # no clue how to add it to the initialized money lololol - 10.47pm
    # found a way lol - 11.22pm








