class Human:
    default_name = "Mike"
    default_age = 28

    def __init__(self, money: int, house: bool, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = money
        self.__house = house

    def info(self):
        print(f"Name is: {self.name}, age is: {self.age}, amount is: {self.__money}")

    @staticmethod
    def default_info():
        print(f"Default name: {Human.default_name}")
        print(f"Default age: {Human.default_age}")

    def make_deal(self, house, price):
        if self.__money >= price:
            self.__money -= price
            self.__house = house
            print(f"Deal successful! {self.name} bought the house.")
        else:
            print(f"{self.name} does not have enough money to buy the house.")

    def provide_name(self):
        return self.name

    def earn_money(self, amount):
        self.__money += amount
        print(f"{self.name} earned {amount} money. Total money now: {self.__money}")

    def buy_house(self, house, discount=0):
        if self.__money >= house.cost - discount:
            self.__money -= house.cost - discount
            self.__house = house
            print(f"Deal successful! {self.name} bought the house.")
        else:
            print(f"{self.name} does not have enough money to buy the house.")


class House:
    def __init__(self, area, price: int):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price - discount


class SmallHouse(House):
    def __init__(self, price):
        super().__init__(area=40, price=price)


human = Human(200000, True, name="Lera", age=33)
house = SmallHouse(150000)
Human.default_info()
human.info()
human.make_deal(house, price=250000)
human.earn_money(200000)
human.make_deal(house, price=250000)


