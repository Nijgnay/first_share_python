class student:
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    @property
    def gender(self):
        return self.__gender

# 正确实例化，用 = 传参
stu = student(name="yj", gender="man")
print(stu.gender)  # 输出 man