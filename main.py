from services import CarWashService
from models import Washer, CarWash, User
from utils import (
    display_admin_menu,
    display_user_menu,
    display_create_order_menu,
    get_input,
    login,
)


def admin_panel(service, user):
    while True:
        display_admin_menu()
        choice = get_input("Choose an option")

        if choice == "1":
            while True:
                try:
                    name = get_input("Enter washer name")
                    experience = int(get_input("Enter washer experience (in years)"))
                    mobile = get_input("Enter washer mobile number")
                    washer = Washer(0, name, experience, mobile)
                    service.add_washer(washer, user)
                    print("Washer added successfully!")
                    break
                except ValueError:
                    print(
                        "Invalid input. Experience must be a number. Please try again."
                    )
                except PermissionError as e:
                    print(e)
                    break

        elif choice == "2":
            while True:
                try:
                    type = get_input(
                        "Enter car wash type (e.g., Full, External, Internal)"
                    )
                    service.validate_car_wash_type(type)
                    duration = int(get_input("Enter wash duration (in minutes)"))
                    price = float(get_input("Enter wash price"))
                    car_wash = CarWash(0, type, duration, price)
                    service.add_or_update_car_wash(car_wash, user)
                    break
                except ValueError as e:
                    print(e)
                    print("Please try again.")
                except PermissionError as e:
                    print(e)
                    break

        elif choice == "3":
            print("Exiting admin panel...")
            break

        else:
            print("Invalid choice! Please try again.")


def user_panel(service, user):
    while True:
        display_user_menu()
        choice = get_input("Choose an option")

        if choice == "1":
            while True:
                display_create_order_menu()
                sub_choice = get_input("Choose an option")

                if sub_choice == "1":
                    available_washers = service.get_available_washers()
                    if available_washers:
                        print("Available Washers:")
                        for washer in available_washers:
                            print(washer)
                    else:
                        print("No washers available at the moment.")

                elif sub_choice == "2":
                    car_wash_types = service.get_car_wash_types()
                    if car_wash_types:
                        print("Available Car Wash Types:")
                        for car_wash in car_wash_types:
                            print(car_wash)
                    else:
                        print("No car wash types available at the moment.")

                elif sub_choice == "3":
                    try:
                        car_wash_id = int(get_input("Enter Car Wash ID"))
                        washer_id = int(get_input("Enter Washer ID"))
                        car_wash = next(
                            cw for cw in service.get_car_wash_types() if cw.id == car_wash_id
                        )
                        washer = next(
                            w for w in service.get_available_washers() if w.id == washer_id
                        )
                        order = service.create_order(car_wash, washer, user)
                    except StopIteration:
                        print("Invalid Car Wash ID or Washer ID. Please try again.")
                    except ValueError as e:
                        print(e)
                        print("Please try again.")
                    break

                elif sub_choice == "4":
                    print("Cancelling order process...")
                    break

                else:
                    print("Invalid choice! Please try again.")

        elif choice == "2":
            print("Exiting user panel...")
            break

        else:
            print("Invalid choice! Please try again.")



def main():
    service = CarWashService()
    try:
        user = login(service)
    except ValueError as e:
        print(e)
        return

    if user.role == "admin":
        admin_panel(service, user)
    else:
        user_panel(service, user)


if __name__ == "__main__":
    main()
