class Feline:
    def __init__(self, name):
        self.name = name
        print('Creating a Feline')

    def meow(self):
        print(f'{self.name}: Meow!')

    def set_name(self, name):
        print(f'{self} setting name: {name}')
        self.name = name


# Lion Class

class Lion(Feline):
    def roar(self):
        print(f'{self.name} roar')

# Tiger class


class Tiger(Feline):
    # overriding a constructor is a bad idea
    def __init__(self):
        # super allows to access the parent
        # if we forget this we'll have a bad time later
        super().__init__('No Name')
        print('Creating Tiger...')

    def stalk(self):
        # have to make sure name is set in the parent
        # this is considered -LBYL ( look before you leap)
        # here we dynamically adding the attribute
        # if not hasattr(self, 'name') : super().setName('No Name')
        print(f'{self.name}: Stalking')

    def rename(self, name):
        super().set_name(name)


a = Feline('Kitty')
print(a)
a.meow()

l = Lion('Leo')
print(l)
l.meow()
l.set_name('Lion Leo')
l.meow()

t = Tiger()  # is Feline but with different constructor
print(t)
t.stalk()
t.rename('Tony')
t.meow()
t.stalk()
