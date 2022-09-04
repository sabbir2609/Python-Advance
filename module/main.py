# OOP => Class (Object)

# import class module

from cat import Cat

# Create a class


def test():
    a = Cat('Kitkat', 2, 'Red')
    b = Cat('Kitty', 2, 'black')
    print(a)
    print(b)
    a.description()
    b.description()

    b.meow()
    a.sleep()
    b.hungry()
    b.eat()


if __name__ == "__main__":
    x = Cat('test')
    print(x)
    test()
