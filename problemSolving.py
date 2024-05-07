diet = input("Do you have any dietary restrictions? (vegetarian, gluten-free):")
if diet == "vegetarian":
    print("salad, rice and beans or yogurt?")
elif diet == "gluten-free":
    print("salad, broccoli soup or eggs?")
else:
    print("salad, burger or mac and cheese?")

meal = input("Select a Meal: (salad, rice and beans, yogurt. broccoli soup, eggs, burger, mac and cheese): ")
plan = input("Do you have a pre-paid meal plan? (yes, no): ")
money = input("How much money do you have? (1, 2, 3, 4, 5, 6, 7, 8, 9, 10): ")
if plan == "no" and money > "5":
    print("Enter payment information: (Debit card, credit card, cash): ")
eat_Outside = True
if eat_Outside: 
    print("Go eat outside")
else: 
    print("Go eat inside")

    


