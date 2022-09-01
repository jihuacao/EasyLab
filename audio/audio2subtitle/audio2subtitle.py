# coding=utf-8
from abc import abstractmethod, ABCMeta

class Audio2Subtitle(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def __call__(self, video):
        pass
    pass