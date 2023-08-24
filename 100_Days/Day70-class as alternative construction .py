class student:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @classmethod
    def forString(cls, string):
        name, age = string.split(',')
        return cls(name, int(age))


person = student.forString("ravi ,9")
print(person._name, person._age)
