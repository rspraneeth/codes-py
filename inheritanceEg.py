class Animal:
    sound = ''

    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.sound} I am {self.name}"


class Pig(Animal):
    sound = "Oink!!"


class Cow(Animal):
    sound = "Moooo!!"


ham = Pig("Hamlet")
print(ham.speak())

milky = Cow("Milky White")
print(milky.speak())
