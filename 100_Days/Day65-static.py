class math:
    def __init__(self, num):
        self.num = num

    def add(self, n):
        self.num = self.num + n

    @staticmethod
    def FunctionName(args1, ages2):
        return args1 + ages2


a = math(5)
a.add(5)
print(a.num)
print(a.FunctionName(5, 5))
# print(math.FunctionName(5, 5))
