class Car:
    wheel = 4
    rate = 0.1

    def __init__(self, c_name, c_brand, c_price, c_colour):
        self.name = c_name
        self.brand = c_brand
        self.price = c_price
        self.colour = c_colour
        self.wheel = 2



c1 = Car("X7", "BMW", 800000, "red")
c2 = Car("X7", "BMW", 800000, "red")

print(c1)
print(c2.wheel)#访问实例属性
print(Car.wheel)#访问类属性
