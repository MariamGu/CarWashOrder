from datetime import datetime


class Washer:
    def __init__(self, id, name, experience, mobile, available=True):
        self.id = id
        self.name = name
        self.experience = experience
        self.mobile = mobile
        self.available = available

    def __repr__(self):
        return (
            f"Washer(id={self.id}, name='{self.name}', experience={self.experience}, "
            f"mobile='{self.mobile}', available={self.available})"
        )


class CarWash:
    def __init__(self, id, type, duration, price):
        self.id = id
        self.type = type
        self.duration = duration
        self.price = price

    def __repr__(self):
        return f"CarWash(id={self.id}, type='{self.type}', duration={self.duration}, price={self.price})"


class User:
    def __init__(self, username, role, mobile, balance=0.0):
        self.username = username
        self.role = role
        self.mobile = mobile
        self.balance = balance

    def __repr__(self):
        return f"User(username='{self.username}', role='{self.role}', mobile='{self.mobile}', balance={self.balance})"


class Order:
    def __init__(self, order_id, car_wash, washer, customer_name, order_time=None):
        self.order_id = order_id
        self.car_wash = car_wash
        self.washer = washer
        self.customer_name = customer_name
        self.order_time = order_time or datetime.now()
        self.status = "ongoing"

    def __repr__(self):
        return (
            f"Order(order_id={self.order_id}, car_wash={self.car_wash}, washer={self.washer}, "
            f"customer_name='{self.customer_name}', order_time='{self.order_time}', status='{self.status}')"
        )

    def to_dict(self):
        return {
            "order_id": self.order_id,
            "car_wash": self.car_wash.__dict__,
            "washer": self.washer.__dict__,
            "customer_name": self.customer_name,
            "order_time": self.order_time.isoformat(),
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, data):
        car_wash = CarWash(**data["car_wash"])
        washer = Washer(**data["washer"])
        order_time = datetime.fromisoformat(data["order_time"])
        return cls(
            data["order_id"], car_wash, washer, data["customer_name"], order_time
        )
