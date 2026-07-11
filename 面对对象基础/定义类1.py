# class car:
#     pass
#
# c1 = car()
# c1.brand = "BMW"
# c1.colour = "red"
# c1.price = 5 * 10 ** 4
#
# print(c1)
# print(c1.brand, c1.colour, c1.price)
# print(c1.__dict__)

class Car:
    wheel = 4
    rate = 0.1

    def __init__(self, c_name, c_brand, c_price, c_colour):
        self.name = c_name
        self.brand = c_brand
        self.price = c_price
        self.colour = c_colour
        self.wheel = 2

    def running(self):
        print(f"{self.brand} {self.name} 正在行驶中")

    def total_cost(self, discount = 1, rate = 0.1):#设置默认值
        total_cost = discount * self.price + rate * self.price
        return total_cost

    def __str__(self):
        return f"{self.name} {self.brand} {self.price} {self.colour}"

    def __eq__(self, other):
        return self.name == other.name and self.brand == other.brand and self.price == other.price and self.colour == other.colour

    def __le__(self, other):
        return self.price <= other.price


c1 = Car("X7", "BMW", 800000, "red")
c2 = Car("X7", "BMW", 800000, "red")

print(c1)
print(c2.wheel)#访问实例属性
print(Car.wheel)#访问类属性

print(c1.brand)

print(c1.__le)