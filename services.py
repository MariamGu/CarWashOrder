import json
import os
import time

from models import CarWash, Washer, Order, User


class CarWashService:
    def __init__(self):
        self.washers = []
        self.car_washes = []
        self.orders = []
        self.users = []
        self.load_data()

    def add_washer(self, washer, user):
        if user.role != "admin":
            raise PermissionError("Only admins can add washers.")
        washer.id = self.generate_id(self.washers)
        self.washers.append(washer)
        self.save_data()

    def add_or_update_car_wash(self, car_wash, user):
        if user.role != "admin":
            raise PermissionError("Only admins can add or update car washes.")
        existing_car_wash = self.find_existing_car_wash(car_wash)
        if existing_car_wash:
            existing_car_wash.duration = car_wash.duration
            existing_car_wash.price = car_wash.price
            print("Car wash type updated successfully!")
        else:
            car_wash.id = self.generate_id(self.car_washes)
            self.car_washes.append(car_wash)
            print("Car wash type added successfully!")
        self.save_data()

    def find_existing_car_wash(self, new_car_wash):
        for car_wash in self.car_washes:
            if car_wash.type == new_car_wash.type:
                return car_wash
        return None

    def create_order(self, car_wash, washer, customer):
        if customer.balance < car_wash.price:
            print("Insufficient balance. Please recharge your account.")
            return

        customer.balance -= car_wash.price
        order_id = self.generate_id(self.orders)
        order = Order(order_id, car_wash, washer, customer.username)
        self.orders.append(order)

        washer.available = False
        self.save_data()

        self.visualize_transaction(car_wash.price)

        print(f"\nOrder created successfully!")
        print(f"Order ID: {order.order_id}")
        print(f"Customer: {customer.username} (Mobile: {customer.mobile})")
        print(f"Washer: {washer.name} (Mobile: {washer.mobile})")
        print(f"Car Wash Type: {car_wash.type}")
        print(f"Duration: {car_wash.duration} minutes")
        print(f"Price: ${car_wash.price:.2f} (charged from your balance)")

        print(f"\nThe washer is on its way!\n")

        return order

    def visualize_transaction(self, amount):
        print("\nProcessing transaction...")
        for _ in range(5):
            print(".", end="", flush=True)
            time.sleep(0.5)
        print(f"\n${amount:.2f} has been charged from your account.\n")

    def complete_order(self, order_id, auto_confirm=False):
        order = next((o for o in self.orders if o.order_id == order_id), None)
        if not order:
            raise ValueError("Invalid Order ID")

        if not auto_confirm:
            confirm = input("Confirm the order completion? (yes/no): ").strip().lower()
            if confirm != "yes":
                print("Order confirmation cancelled.")
                return

        order.washer.available = True
        order.status = "completed"
        self.save_data()
        print("Order completed successfully!")

    def get_available_washers(self):
        return [w for w in self.washers if w.available]

    def get_car_wash_types(self):
        return self.car_washes

    def save_data(self):
        data = {
            "washers": [w.__dict__ for w in self.washers],
            "car_washes": [cw.__dict__ for cw in self.car_washes],
            "orders": [o.to_dict() for o in self.orders],
            "users": [u.__dict__ for u in self.users],
        }
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        if not os.path.exists("data.json"):
            return

        with open("data.json", "r") as f:
            data = json.load(f)
            self.washers = [Washer(**w) for w in data.get("washers", [])]
            self.car_washes = [CarWash(**cw) for cw in data.get("car_washes", [])]
            self.orders = [Order.from_dict(o) for o in data.get("orders", [])]
            self.users = [User(**u) for u in data.get("users", [])]

    def add_user(self, user):
        self.users.append(user)
        self.save_data()

    def find_user(self, username):
        return next((u for u in self.users if u.username == username), None)

    @staticmethod
    def generate_id(items):
        if not items:
            return 1
        if isinstance(items[0], Order):
            return max([item.order_id for item in items], default=0) + 1
        else:
            return max([item.id for item in items], default=0) + 1

    @staticmethod
    def validate_car_wash_type(car_wash_type):
        valid_types = ["Full", "External", "Internal"]
        if car_wash_type not in valid_types:
            raise ValueError(f"Invalid car wash type. Must be one of {valid_types}.")
