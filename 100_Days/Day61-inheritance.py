class employee:
    def __init__(self, name, id):
        self._name = name
        self._id = id

    def showData(self):
        print("value:", self._id, self._name)


class programmer(employee):
    def show(self):
        print("hii hello")


aa = employee("Rohan Das", 40)
aa.showData()

bb = programmer("ravi", 100)
bb.show()
bb.showData()
