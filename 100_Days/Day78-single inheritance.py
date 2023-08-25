class animal:
    def __init__(self, name, species):
        self.name = name
        self.speciies = species

    def make_sound(self):
        print("sound made of by the animals")


class dog (animal):
    def __init__(self, name, breed):
        #        super().__init__()
        #        super.__init__ is used to call a parent class constructor from child class constructor
        animal.__init__(self, name, species="Dog")
        self.breed = breed

    def make_sound(self):
        print("bark")


d = dog("Dog", "doggermn")
d.make_sound()
a = animal("Dog", "Dog")
a.make_sound()
