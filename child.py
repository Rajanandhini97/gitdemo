from oopsdemo import Calculator

class childimp(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 8)

    def getCompletedata(self):
        return self.num2 + self.num + self.Summation()

obj = childimp()
print(obj.getCompletedata())