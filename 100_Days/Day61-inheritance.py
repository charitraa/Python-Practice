class employee:
    def __init__(self, name, id):
        self._name = name
        self._id = id

    def showData(self):
        print("value:", self._id, self._name)


aa = employee("Rohan Das", 40)
aa.showData()
