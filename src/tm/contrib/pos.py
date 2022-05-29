import enum
from collections import namedtuple

Position = namedtuple("Position", ("x", "y"))

VerticesBox = namedtuple("VerticesBox", ("x1", "y1", "x2", "y2"))
SideLengthBox = namedtuple("SideLengthBox", ("x", "y", "w", "h"))


class SimpleBox:

    def __init__(self, x, y, w, h):
        self._pos_x = x
        self._pos_y = y
        self._pos_w = w
        self._pos_h = h

    @property
    def x(self):
        return self._pos_x

    @property
    def y(self):
        return self._pos_y

    @property
    def w(self):
        return self._pos_w

    @property
    def h(self):
        return self._pos_h

    @property
    def x1(self):
        return self._pos_x

    @property
    def y1(self):
        return self._pos_y

    @property
    def x2(self):
        return self._pos_x + self._pos_w

    @property
    def y2(self):
        return self._pos_y + self._pos_h

    def get_vertices(self):
        return VerticesBox(self._pos_x, self._pos_y, self._pos_x + self._pos_w, self._pos_y + self._pos_h)

    def get_side_lengths(self):
        return SideLengthBox(self._pos_x, self._pos_y, self._pos_w, self._pos_h)


class Direction(enum.IntEnum):
    UP = 0
    DOWN = 1
    SELECT = 2
