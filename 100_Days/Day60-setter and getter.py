# # this is the oops

# # class
# class myclass:
#     # constructors
#     def __init__(self, value1):
#         self.value2 = value1

#     # getter

#     @property
#     def value(self):
#         return self.value2

#     # setter
#     @value.setter
#     def value3(self, value4):
#         self.value2 = value4/10

#     # function
#     def show(self):
#         print("my class object", self.value2)


# # oobject
# obj = myclass(10)
# # obj.value3 = 20
# obj.show()


class fruit:
    def __init__(self, name: str):
        self._name = name

    @property
    def get_name(self):
        print("getting name.")
        return self._name

    @get_name.setter
    def get_name(self, new_name: str):
        self._name = new_name


fd = fruit("mango")
fd.get_name = "shrestha"
print(fd.get_name)

# if __name__ == "__main__":

#     fd = fruit("ravi")
#     fd.set_name("ravi")
#     print(fd.get_name())
