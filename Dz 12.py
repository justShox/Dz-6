# Examples for every topic

# 1
# Types
num = 21
print(type(num))

fl = 12.4
print(type(fl))

name = 'Jonh'
print(type(name))

boo = True
print(boo)

# 2
# Conditions
x = 10
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")

# 3
# List
# Tumple
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

# 4
# Cycle
for i in range(5):
    print(i)

# 5
# List
my_list5 = [1, 2, 3, 4, 5]
my_list5.append(6)
my_list5.pop()
first_element = my_tuple[0]


# 6
# Set
dict = {"apple": "red", "banana": "yellow"}
set = {1, 2, 3, 4, 5}

# 7 в самом низу

# 8
# Anonymous func
import math

sqrt = lambda n: math.sqrt(n)
print(sqrt(9))


# 9
# Class
class MyClass:
    def __init__(self, x):
        self.x = x

    def print_x(self):
        print(self.x)


my_object = MyClass(10)
my_object.print_x()


# 10
# Inheritance
class ParentClass:
    def __init__(self, y):
        self.y = y

    @property
    def x(self):
        return self.y

    @classmethod
    def example_classmethod(cls):
        print("This is a class method!")


class ChildClass(ParentClass):
    def print_x(self):
        print(self.x)


child = ChildClass(10)
child.print_x()
ChildClass.example_classmethod()

# 7
# Working with requests
import requests

API = '04ce9501ff1973178da581c5d24d4b4f'


def get_weather_info():
    city = input("Введите название города: ")

    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric")

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        visibility = data['visibility']
        visibility_km = visibility / 1000
        print(f"Температура: {main['temp']}°C")
        print(f"Влажность: {main['humidity']}%")
        print(f"Видимость: {visibility_km} км")
    else:
        print("Город не найден. Пожалуйста, попробуйте еще раз.")


while True:
    get_weather_info()
