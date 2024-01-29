class student:
    def __init__(self):
        self.__name = "ravi"  # privated  variable


a = student()
print(a._student__name)  # type: ignore
