from abc import ABCMeta,abstractmethod


class Processor:

    __metaclass__ = ABCMeta

    @abstractmethod
    def process(self,*args,**kwargs):
        pass
