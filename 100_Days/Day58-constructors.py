class person:
    # constructor
    def __init__(self, n, o):
        self.name = n
        self.occ = o

    def info(self):
        print("Name:", self.name, "occ:", self.occ)


a = person("tavi", "HR").info()
b = person("rabina", "CA").info()
