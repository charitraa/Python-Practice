class ravi:
    name = "ravi"

    def __init__(self, ravi):
        self.ravi = ravi

    def __len__(self):
        i = 0
        for c in self.name:
            i = i+1
        return i

    def __str__(self):
        return "ravi"


e = ravi("avi")
print(e.ravi)
# print(e.name)  # prints 'ravi'
# print(len(e.name))
# print(len(e))
