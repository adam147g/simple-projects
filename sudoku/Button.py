from Colors import *

class Button:
    def __init__(self, position, size, number=False,name=None):
        self._position = position
        self._size = size
        self._active = False
        if number:
            self._color = LIGHT_BLUE
        else:
            self._color = WHITE
        self._number = number
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
            if self._number:
                self._color = BLUE
            else:
                self._color = GRAY
        else:
            if self._number:
                self._color = LIGHT_BLUE
            else:
                self._color = WHITE

    @property
    def color(self):
        return self._color

    @property
    def number(self):
        return self._number

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
