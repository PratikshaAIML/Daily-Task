# Login function
def login():
    print("Welcome to the Online Restaurant Management System!")
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == "Pratiksha" and password == "Pratiksha123":
            print("Login successful!\n")
            break
        else:
            print("Invalid credentials. Please try again.\n")

# Function to display category menu
def display_category_menu():
    print("-------- MENU CATEGORIES --------")
    print("1. Starters")
    print("2. Main Course")
    print("3. Desserts")
    print("4. Exit and Finalize Order")
    print("---------------------------------\n")

# Function to display items within a category
def display_items(category):
    print(f"-------- {category.upper()} --------")
    menu = {"Starters": starters, "Main Course": main_course, "Desserts": desserts}
    for index, (item, price) in enumerate(menu[category].items(), start=1):
        print(f"{index}. {item} - ₹{price}")
    print("--------------------------")
    return list(menu[category].items())  # Return the list of items for selection by index

# Function to place an order
def place_order():
    order = []
    total_cost = 0
    while True:
        display_category_menu()
        choice = int(input("Select a category: "))
        if choice == 1:
            category = "Starters"
        elif choice == 2:
            category = "Main Course"
        elif choice == 3:
            category = "Desserts"
        elif choice == 4:
            print("\nFinalizing your order...")
            break
        else:
            print("Invalid choice. Please try again.\n")
            continue

        # Display items in the selected category
        if choice in [1, 2, 3]:
            items = display_items(category)
            item_choice = int(input("Enter the number of the item you want to order: "))
            if 1 <= item_choice <= len(items):
                selected_item, price = items[item_choice - 1]
                quantity = int(input(f"Enter the quantity for {selected_item}: "))
                order.append((selected_item, quantity, price * quantity))
                total_cost += price * quantity
                print(f"{quantity} x {selected_item} added to your order.\n")
            else:
                print("Invalid item number. Please try again.\n")

    return order, total_cost

# Function to generate the bill
def generate_bill(order, total_cost):
    print("\n-------- BILL --------")
    for item, quantity, total in order:
        print(f"{item} (x{quantity}) - ₹{total}")
    print("----------------------")
    print(f"Total Cost: ₹{total_cost}")
    print("----------------------")
    print("Thank you for ordering with us! Enjoy your meal!\n")

# Food menu data
starters = {
    "Spring Rolls": 220,
    "Paneer Chilli": 200,
    "Soup": 100,
    "Chicken Chilli": 250,
    "Chicken 65": 280,
    "Veg Crispy": 150,
    "Cheese Sigar Roll": 320
}
main_course = {
    "Paneer Butter Masala": 350,
    "Chicken Handi": 500,
    "Veg Biryani": 400,
    "Chicken Biryani": 550,
    "Roti": 40,
    "Butter Roti": 45,
    "Jeera Rice": 350
}
desserts = {
    "Ice Cream": 100,
    "Gulab Jamun": 80,
    "Brownie": 150
}

# Main program
def main():
    login()
    while True:
        print("\n1. Place Order")
        print("2. Exit")
        user_choice = int(input("Your choice: "))
        if user_choice == 1:
            order, total_cost = place_order()
            generate_bill(order, total_cost)
        elif user_choice == 2:
            print("Thank you for visiting! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
main()
