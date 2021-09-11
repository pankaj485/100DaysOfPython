from data import MENU
from data import resources

# quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01

turn_off = False
water_left = resources["water"]
milk_left = resources["milk"]
coffee_left = resources["coffee"]
money_earned = 0

while not turn_off:

    def print_report():
        print("==== report ====")
        print("water left:", water_left, "ml")
        print("milk left:", milk_left, "ml")
        print("coffee left:", coffee_left, "ml")
        print("money earned:$", money_earned)


    def make_purchase(coffee_type, actual_cost, user_paid_amount):
        global water_left, milk_left, coffee_left, money_earned, amount_to_return
        change_amount = user_paid_amount - actual_cost

        if coffee_type == "latte":
            print("Here is your latte. Enjoy!")
            money_earned += 2.5
            water_left -= 200
            coffee_left -= 24
            milk_left -= 150

        elif coffee_type == "cappuccino":
            print("Here is your cappuccino. Enjoy!")
            money_earned += 3
            water_left -= 250
            coffee_left -= 24
            milk_left -= 100

        elif coffee_type == "espresso":
            print("Here is your espresso. Enjoy!")
            money_earned += 1.5
            water_left -= 50
            coffee_left -= 18

        if change_amount > 0:
            return f"Here is ${'{:.2f}'.format(change_amount)} dollars in change."


    def check_availability(coffee_type):
        global turn_off

        coffee_selected = MENU[coffee_type]
        ingredients = coffee_selected["ingredients"]
        water = ingredients["water"]
        milk = ingredients["milk"]
        coffee = ingredients["coffee"]
        cost = coffee_selected["cost"]

        cost_qualified = total_user_paid_amount >= cost
        conditions_favourable = cost_qualified and water_left >= water and milk_left >= milk and coffee_left >= coffee

        if conditions_favourable:
            purchase_status = make_purchase(coffee_type, cost, total_user_paid_amount)
            if purchase_status:
                print(purchase_status)
            # print_report()
            print("===========================")

        elif water_left < water:
            turn_off = True
            print("Sorry there is not enough water.")

        elif milk_left < milk:
            turn_off = True
            print("Sorry there is not enough milk.")

        elif coffee_left < coffee:
            turn_off = True
            print("Sorry there is not enough coffee.")

        elif total_user_paid_amount < cost:
            print("Sorry that's not enough money. Money refunded")


    print_report()

    user_input = input("what would you like? (espresso/latte/cappuccino): ")

    if user_input == "report":
        print_report()

    elif user_input == "end":
        turn_off = True
        print("==== machine turned off ===")

    else:
        print("what amount are you paying?")
        input_quarters = float(input("quarters:"))
        input_dimes = float(input("dimes:"))
        input_nickles = float(input("nickles:"))
        input_pennies = float(input("pennies"))

        total_user_paid_amount = (0.25 * input_quarters) + (0.10 * input_dimes) + (0.05 * input_nickles) + (
                0.01 * input_pennies)

        amount_to_return = 0

        check_availability(user_input)
