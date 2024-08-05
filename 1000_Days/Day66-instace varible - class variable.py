class employe:
    companyName = "ABC"  # class variable

    def __init__(self, name):
        self.name = name
        self.rais = 1

    def show(self):
        print(f"value:{self.name} and {self.rais} ans {self.companyName}")


emp1 = employe("rvi")
emp1.rais = 2  # insatnce variable
emp1.companyName = 'ravi'
emp1.show()
emp2 = employe('rohan')
# employe.show(emp1)
emp2.show()
