from abc import *
# abstract class of background and airplane or anything else 
class AbstractCharacter(metaclass=ABCMeta):
    @abstractmethod
    def goto(self, x, y):
        pass
 
    @abstractmethod
    def update(self, dt, screen):
        pass

    @abstractmethod
    def draw(self, screen):
        pass