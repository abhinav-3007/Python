class Animal:
    def __init__(self, name, breed):
        self._name = name
        self._breed = breed

    def wags(self):
        print(self._name, "is happy")

    def set_name(self, name):
        self._name = name


class Dog(Animal):
    def __init__(self, name, breed, colour):
        super().__init__(name, breed)
        self.colour = colour

    def speak(self):
        print(self._name, "barks")

    def wags(self):
        super().wags()
        print('sad')


class Cat(Animal):
    def __init__(self, name, breed, fur):
        super().__init__(name, breed)
        self.fur = fur

    def speak(self):
        print(self._name, "meows")


class Kitten(Cat):
    def __init__(self, name, breed, fur, age):
        super().__init__(name, breed, fur)
        self.age = age


dog = Dog("Tipsy", "Beagle", 'brown')
cat = Cat("Leslie", "Super Cat", 'black')

dog.wags()
