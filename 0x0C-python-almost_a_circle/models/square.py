#!/usr/bin/python3
'''A square class that inherits from rectangle'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''A subclass of the supersubclass Rectangle'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Instatiation of a square class'''

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''size getter'''

        return self.width

    @size.setter
    def size(self, value):
        '''size setter
        args: size
        '''

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def __str__(self):
        '''beautifies the output'''

        s = (
            f"[{Square.__name__}] ({self.id}) "
            f"{self.x}/{self.y} - {self.size}"
        )
        return s

    def update(self, *args, **kwargs):
        '''assigns an argument to each attribute'''

        if args and len(args):
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''returns the dictionary representation of a square'''

        dict = {'id': self.id, 'x': self.x,
                'size': self.width, 'y': self.y}
        return dict
