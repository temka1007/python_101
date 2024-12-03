class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting!")

    def roll_over(self):
        print(f"{self.name} rolled over!")


german_shepherd = Dog("Rex", 12)

german_shepherd.sit()
german_shepherd.roll_over()


class Restaurant:
    def __init__(self, name, sign_cuisine, status):
        self.name = name
        self.sign_cuisine = sign_cuisine
        self.status = status

    def describe_restaurant(self):
        print(f"This restraurant's name is {self.name}")
        print(f"The signiture cuisine is {self.sign_cuisine}")

    def open_restuarant(self):
        if self.status == True:
            print("The restuarant is open!")
        else:
            print("The restuarant is closed!")


gordan_ramsay = Restaurant("Hell's kitchen", "Beef wellington", False)

gordan_ramsay.describe_restaurant()
gordan_ramsay.open_restuarant()


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descripetive_name(self):
        long_name = f"{self.year} {self.brand} {self.model}"
        return long_name

    def read_odometer(self):
        print(f"Car's odomater is {self.odometer_reading} mile")

    def update_odometer(self, mileage):
        self.odometer_reading = self.odometer_reading + mileage


dealership_car = Car("Toyota", "Supra", "2020")

print(dealership_car.get_descripetive_name())
dealership_car.read_odometer()
dealership_car.update_odometer(200)
dealership_car.read_odometer()
dealership_car.update_odometer(100)
dealership_car.read_odometer()
