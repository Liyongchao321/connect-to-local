from datetime import datetime
from abc import abstractmethod, ABC
def alert(e):
    print(e)

def alert_with_exp(cls):
    cls.__init__()
    print(cls.__dir__())
    func = cls.__getattribute__('calc')
    def getarg(*arg, **kvargs):
        try:
            func(*arg, **kvargs)
        except ZeroDivisionError as e:
            # func.__class__.__self__.status = 'not ok haha'
            print('ERR:')
            print(func.__format__())
            print(func.__name__)
            alert(e)

    return getarg
    

@alert_with_exp
def calc(a, b):
    return a/b

@alert_with_exp
class Power:
    def __init__(self):
        self.res = None

    # @alert_with_exp
    def calc(self,a,b):
        return a/b
        # try:
        #     return a/b
        # except ZeroDivisionError as e:
        #     # print(e)
        #     return None

class People(ABC):
    def __init__(self, name):
        self.name = name
        self.res = None
        self.status = 'ok'

class Father(People):
    def __init__(self, name):
        super().__init__(name)
        self.power = Power()

    def use_power(self, a, b):
        res = self.power.calc(a,b)
        self.res =  "{} {}".format(self.name, res)

class Son(People):
    def __init__(self, name):
        self.name = name
        self.father = Father("f{}".format(name))
        self.res = None
        self.status = 'ok'

    # @alert_with_exp
    def use_father_power(self, a, b):
        res = self.father.power.calc(a,b)
        self.res =  "{} {}".format(self.name, res)

    # def use_father_power(self, a, b):
    #     # res = self.father.power.calc(a,b)
    #     # if res == None:
    #     #     self.status = 'not ok'
    #     # else:
    #     #     self.res =  "{} {}".format(self.name, res)
    #     try:
    #         res = self.father.power.calc(a,b)
    #         self.res =  "{} {}".format(self.name, res)
    #     except ZeroDivisionError as e:
    #         self.status = 'not ok'
    #         print(self.__class__.__name__, self.name, e)

if __name__ == "__main__":
    # father = Father("ff")
    # father.use_power(2,0)
    # print("father res= ", father.res)
    # print("father status=", father.status)

    son = Son("ss")
    son.use_father_power(2,0)
    print("son res= ", son.res)
    print("son status=", son.status)
