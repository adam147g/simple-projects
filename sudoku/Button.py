class Button:
    def __init__(self, position, size, name=None):
        self.position = position
        self.size = size
        self.active = False
        if name is None:
            self.name = ""
        else:
            self.name = name
