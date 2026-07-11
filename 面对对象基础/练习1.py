"""class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} 需要进食")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def eat(self):
        super().eat()
        print(f"小狗{self.name}啃骨头")
    def bark(self):
        print("汪汪叫!")

dog = Dog("旺财")
dog.eat()
dog.bark()
"""

"""class Book:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price >= 0:
            self.__price = price
        else:
            print("价格不能小于0!!!")


book = Book("格林童话", 91)
print(book.price)
book.price = 78
print(book.price)
book.price = -91
print(book.price)


"""
"""
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.__base_salary = base_salary

    @property
    def base_salary(self):
        return self.__base_salary

    @base_salary.setter
    def base_salary(self, base_salary):
        if base_salary >= 2000:
            self.__base_salary = base_salary
        else:
            print("太低!!拒绝")

    def get_salary(self):
        return self.__base_salary

class FullTime(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def get_salary(self):
        return self.base_salary + self.bonus

class PartTime(Employee):
    def __init__(self, name, base_salary, hour, hour_pay):
        super().__init__(name, base_salary)
        self.hour = hour
        self.hour_pay = hour_pay

    def get_salary(self):
        return self.hour * self.hour_pay

def print_total(emp):
    print(f"{emp.name}的收入是:{emp.get_salary()}")

ft = FullTime("老王", 5000, 500)
print_total(ft)
"""
"""
class Graph:
    def __init__(self, shape):
        self.shape = shape
    def get_perimeter(self):
        pass
    def get_area(self):
        pass

class Square(Graph):
    def __init__(self, shape, side):
        super().__init__(shape)
        self.side = side
    def get_perimeter(self):
        return 4 * self.side
    def get_area(self):
        return self.side ** 2

class Triangle(Graph):
    def __init__(self, shape, a, b):
        super().__init__(shape)
        self.a = a
        self.b = b
    def get_perimeter(self):
        return round(self.a + self.b + (self.a**2 + self.b**2) ** 0.5, 1)
    def get_area(self):
        return (self.a * self.b) * 0.5

def print_perimeter_area(graph):
    print(f"{graph.shape}的周长是{graph.get_perimeter()},面积是{graph.get_area()}")

zf = Square("正方形", 3)
sjx = Triangle("三角形", 4, 5)
print_perimeter_area(sjx)
"""

"""class Car:
    def __init__(self, engine = 9178):
        self.__engine = engine
    def get_engine(self):
        return self.__engine

class SportCar(Car):
    def __init__(self, engine = 9178):
        super().__init__(engine)
    def get_engine(self):
        base = super().get_engine()
        return f"{base}运动改装版引擎"


yj = SportCar()
print(yj.get_engine())
"""
