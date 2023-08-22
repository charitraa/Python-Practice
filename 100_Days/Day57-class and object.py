class Person:
    name = "ravi"
    occupation = "fullstack"
    network = 10

    def info(self):
        print("name:", self.name)
        print(f"i am {self.name}")


a = Person()
a.name = "rabi"
print(a.name)
a.info()
