from Colors import *
from ButtonType import ButtonType


class Button:
    def __init__(self, position, size, type=None, name=None):
        self._position = position
        self._size = size
        self._active = False
        if type == ButtonType.NUMBERS_TO_CHOOSE:
            self._color = LIGHT_BLUE
        elif type == ButtonType.BOARD:
            self._color = WHITE
        elif type == ButtonType.CONFIRM:
            self._color = LIGHT_GREEN

        self._type = type
        if name is None:
            self._name = ""
        else:
            self._name = name

    @property
    def position(self):
        return self._position

    @property
    def size(self):
        return self._size

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value):
        self._active = value
        if self._active:
            if self.type == ButtonType.NUMBERS_TO_CHOOSE:
                self._color = BLUE
            elif self.type == ButtonType.BOARD:
                self._color = GRAY
            elif self.type == ButtonType.CONFIRM:
                self._color = GREEN
        else:
            if self.type == ButtonType.NUMBERS_TO_CHOOSE:
                self._color = LIGHT_BLUE
            elif self.type == ButtonType.BOARD:
                self._color = WHITE
            elif self.type == ButtonType.CONFIRM:
                self._color = LIGHT_GREEN


    @property
    def color(self):
        return self._color

    @property
    def type(self):
        return self._type

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
