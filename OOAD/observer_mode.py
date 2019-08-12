from abc import ABC, abstractmethod

class Subject(ABC):

    @abstractmethod
    def register_observer(self, observer):
        pass
    
    @abstractmethod
    def remove_observer(self, observer):
        pass
    
    @abstractmethod
    def display_subjet(self, observer):
        pass

class WeatherData(Subject):
    def __init__(self, observer):
        self.observer = observer

