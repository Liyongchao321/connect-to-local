

from abc import ABC, abstractmethod

class Duck(ABC):
    def __init__(self, flybehavior, quackbehavior):
        self.flybehavior = flybehavior
        self.quackbehavior = quackbehavior
    
    @abstractmethod
    def display(self):
        raise NotImplementedError
        """
        :print the name of the duck
        """

    @abstractmethod
    def swim(self):
        raise NotImplementedError
        """
        :print if it can swim
        """

    def performfly(self):
        self.flybehavior.fly()
    
    def performquack(self):
        self.quackbehavior.quack()

class FlyBehavior(object):

    @abstractmethod
    def fly(self):
        raise NotImplementedError
        """
        :print if it can fly
        """

class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying!!!")

class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I can't fly")

class QuackBehavior(object):

    @abstractmethod
    def quack(self):
        raise NotImplementedError
        """
        :print different kinds of quark
        """

class Quack(QuackBehavior):
    def quack(self):
        print("Quark")

class MuteQuack(QuackBehavior):
    def quack(self):
        print("<<slience>>")

class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak")

class MallardDuck(Duck):

    def swim(self):
        print("I can swim")

    def display(self):
        print("I am a real Mallard duck")

if __name__=='__main__':
    mallardduck = MallardDuck(FlyWithWings(), Quack())
    mallardduck.swim()
    mallardduck.display()
    mallardduck.performfly()
    mallardduck.performquack()
    
        
    