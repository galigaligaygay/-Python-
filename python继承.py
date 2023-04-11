class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


# 使用 Person 来创建对象，然后执行 printname 方法：

x = Person("Bill", "Gates")
x.printname()


class Student(Person):
    def __init__(self, fname, lname, year):  # 添加属性
        super().__init__(fname, lname)

        self.graduationyear = year

    def welcome(self):  # 添加方法
        print('Welcome', self.firstname, self.lastname, 'to the class of', self.graduationyear)


x = Student("Elon", "Musk", 2019)
x.welcome()
print(x.graduationyear)
