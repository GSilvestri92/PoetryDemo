from abc import ABC, abstractmethod

class Operator(ABC):

    @abstractmethod
    def operation(self,input:list):
        pass

    
    
    
