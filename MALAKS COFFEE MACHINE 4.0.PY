import random
#a few issues i had with the last verions that i wanna address here
#the functions are all messy and in the first version i forgot the while loop
#starting with the functions from prev attempts 
#av is available lol 
#fix deduction system
#fix money storing system
#strips are so cool

def initial_coffee_resources():
    water_av = random.randint(800, 1000)
    coffee_av = random.randint(400, 800)
    milk_av = random.randint(200, 400)
    money_av = 0
    return water_av, coffee_av, milk_av, money_av

def check_resources(water, coffee, milk, required_water, required_coffee, required_milk):
    return (
        water >= required_water
        and coffee >= required_coffee
        and milk >= required_milk
    )
#issue with the third version was deduct 
#issue fixed
def deduct_resources(beverage, water_av, coffee_av, milk_av):
    water_new = water_av - beverage["water"]
    coffee_new = coffee_av - beverage["coffee"]
    milk_new = milk_av - beverage["milk"]
    
    if water_new < 0 or coffee_new < 0 or milk_new < 0:
        print("Not enough resources.")
        return water_av, coffee_av, milk_av
    
    return water_new, coffee_new, milk_new
#adding only water and coffee for making the espresso
def make_coffee(choice):
    if choice == "Espresso":
        print("Adding water...")
        print("Adding coffee...")
    elif choice == "Latte":
        print("Adding water...")
        print("Adding coffee...")
        print("Adding milk...")
    elif choice == "Cappuccino":
        print("Adding water...")
        print("Adding coffee...")
        print("Adding milk...")

water_av, coffee_av, milk_av, money_av = initial_coffee_resources()
orders_history = []  #for report lols 

while True:
    print("Current Coffee Machine Resources:")
    print(f"Water: {water_av} ml")
    print(f"Coffee Beans: {coffee_av} mg")
    print(f"Milk: {milk_av} ml")
    print(f"Money: {money_av} JD")

    Espresso = {"water": 80, "coffee": 200, "milk": 0, "cost": 2}
    Latte = {"water": 100, "coffee": 100, "milk": 100, "cost": 3}
    Cappuccino = {"water": 100, "coffee": 75, "milk": 150, "cost": 3.5}

    choice = input("What would you like? (Espresso/Latte/Cappuccino): ")
    #i wanna find a way to make it accept both uppercase and lower case choices

    if choice not in ["Espresso", "Latte", "Cappuccino"]:
        print("Invalid choice, please enter again.")
        continue

    beverage = None
    if choice == "Espresso":
        beverage = Espresso
    elif choice == "Latte":
        beverage = Latte
    elif choice == "Cappuccino":
        beverage = Cappuccino

    print(f"Checking resources for {choice}...")
    if not check_resources(water_av, coffee_av, milk_av, beverage["water"], beverage["coffee"], beverage["milk"]):
        print("Not enough resources. Please choose another option.")
        continue
#adding original paying method from version 2 
    money_message = f"That would be: JD{beverage['cost']:.2f}"
    remainder = 0  # Initialize remainder before the loop
    while True:
        amount_paid = float(input(f"{money_message}\nPay ahead: JD"))

        if amount_paid == beverage['cost']:
            print(f"Thank you! Your remainder is 0 JD")
            money_av += amount_paid  
            break
        elif amount_paid > beverage['cost']:
            remainder = amount_paid - beverage['cost']
            print(f"Thank you! Your remainder is JD{remainder:.2f}")
            money_av += beverage['cost']    
            break
        else:
            print(f"Insufficient payment. Please pay JD{beverage['cost']:.2f}")


    make_coffee(choice)  
    water_av, coffee_av, milk_av = deduct_resources(beverage, water_av, coffee_av, milk_av)
    print("Updated resources after making", choice)
    print(f"Water: {water_av} ml, Coffee Beans: {coffee_av} mg, Milk: {milk_av} ml, Money: {money_av} JD")

    #for report you get a report of each drink
    orders_history.append({
        'beverage': choice,
        'resources_used': {
            'water': beverage['water'],
            'coffee': beverage['coffee'],
            'milk': beverage['milk']
        },
        'amount_paid': amount_paid,
        'remainder': remainder #fix issue here when theres no remainder 
    })
#fixed this 5 times at this point to make it loop to the start (hardest part)
    choice = input("Would you like to order something else? (yes/no): ")
    while choice not in ['yes', 'no']:
        print("Invalid option. Please enter 'yes' or 'no'.")
        choice = input("Would you like to order something else? (yes/no): ")

    if choice == 'no':
        report_input = input("Press Enter for a report or type 'off' to exit: ")
        if report_input.strip() == '':
            print("\n===== REPORT =====")
            for order in orders_history:
                print(f"Beverage: {order['beverage']}")
                print(f"Resources Used: Water - {order['resources_used']['water']} ml, Coffee Beans - {order['resources_used']['coffee']} mg, Milk - {order['resources_used']['milk']} ml")
                print(f"Amount Paid: JD{order['amount_paid']:.2f}")
                print(f"Remainder: JD{order['remainder']:.2f}")
                print("------------------------------")
            print("Turning off the coffee machine. Goodbye!")
            break

 

