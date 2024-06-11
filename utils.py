from models import User


def display_admin_menu():
    print("\n==== Admin Panel ====")
    print("1. Add Washer")
    print("2. Add Car Wash Type")
    print("3. Exit")
    print("=====================")


def display_user_menu():
    print("\n==== Car Wash Service Menu ====")
    print("1. Create Order")
    print("2. Exit")
    print("===============================")


def display_create_order_menu():
    print("\n==== Create Order Menu ====")
    print("1. View Available Washers")
    print("2. View Car Wash Types")
    print("3. Proceed with Order")
    print("4. Cancel")
    print("===========================")


def get_input(prompt):
    return input(f"{prompt}: ").strip()


def login(service):
    while True:
        try:
            username = get_input("Enter username")
            role = get_input("Enter role (admin/user)").lower()
            if role not in ["admin", "user"]:
                raise ValueError("Invalid role. Must be 'admin' or 'user'.")

            mobile = get_input("Enter your mobile number")

            user = service.find_user(username)
            if not user:
                if role == "admin":
                    user = User(username, role, mobile)
                    service.add_user(user)
                else:
                    balance = float(get_input("Enter initial balance"))
                    user = User(username, role, mobile, balance)
                    service.add_user(user)
            return user
        except ValueError as e:
            print(e)
            print("Please try again.")
