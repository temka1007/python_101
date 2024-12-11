class Restaurant:

    def __init__(self, name, sign_cuisine, status):
        self.name = name
        self.sign_cuisine = sign_cuisine
        self.status = status

    def describe_restaurant(self):
        return f"This is restuarant naem is{self.name}, and it have signature cuisine name {self.sign_cuisine}"

    def open_restaurant(self):
        if self.status == True:
            return "Open!"
        else:
            return "Closed!"


new_york = Restaurant("Luigi", "Hawaii Pizza", False)
chigago = Restaurant("Boston Horders", "Olive Pasta", True)
new_jersey = Restaurant("Pizza Hat", "Double cheese dip", False)

print(
    new_jersey.open_restaurant(),
    chigago.open_restaurant(),
    new_jersey.open_restaurant(),
)


class Employee:
    raise_amt = 1.05
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.mail = f"{first}{last}gmail.com"

        Employee.num_of_emps += 1

    def full_name(self):
        return "{}{}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    @classmethod
    def set_rasie_amount(cls, amount):
        cls.amount = amount


emp_1 = Employee("Corey", "Wayne", 50000)
emp_2 = Employee("Bruce", "Wayne", 1000000)


print(emp_1.raise_amount)

emp_1.apply_raise()

Employee.set_rasie_amount(1.07)

print(Employee.raise_amt)
