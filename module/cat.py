# The Cat Class
# self is the first param
# 'self' is refer to 'this' kw in other language
# when object created it becomes an instance
# we can have multiple instances

class Cat:
    name = ''
    age = 0
    color = ''

    # __init__ <= constructor
    def __init__(self, name, age=0, color='white'):   #self required, name and other params
        self.name = name
        self.age = age
        self.color = color
        print(f'Constructor for {self.name}')

    def meow(self):
        print(f'{self.name} Meow!')

    def sleep(self):
        print(f'{self.name} 🕑😿 zzz')

    def hungry(self):
        for i in range(5):
            self.meow()

    def eat(self):
        print(f'{self.name} 😿 nom nom nom')

    def description(self):
        print(f'{self.name} is a {self.color} cat, who is {self.age} years old.')