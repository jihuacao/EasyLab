# coding=utf-8
from abc import abstractmethod, ABCMeta

class VideoWithAudio(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def __call__(self, video, audio):
        pass
    pass