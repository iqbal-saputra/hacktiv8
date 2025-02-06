class IbuKucing:
    def __init__(self, name):
        self.name = name

        # private attribute
        self.__secret = "ini secret ibu kucing"

    def greet(self):
        print("meong!")


class AnakKucing(IbuKucing):
    def __init__(self, name):
        self.canRun = True
        super().__init__(name)

    # overriding
    def greet(self):
        print("hello world!")

    # overloading -> tidak support python
    # def greet(self, param1):
    # print("hello world! + param1")


print("Module")
