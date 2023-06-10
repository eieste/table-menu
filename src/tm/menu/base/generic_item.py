import logging

from tm.config import settings
from tm.contrib.pos import Position, VerticesBox
from tm.menu.base.draw import default_text

log = logging.getLogger()


class MenuItem:

    def __init__(self, parent=None, title=None):
        self._parent = parent
        self._title = title

    def __repr__(self):
        return f"<MenuItem {self.title()}>"

    def title(self):
        if type(self._title) is str:
            return str(self._title)
        else:
            return self._title(self)

    def get_parent(self):
        return self._parent

    def get_menu_manager(self):
        return self._parent.get_menu_manager()

    def is_selected(self):
        return self.get_menu_manager().turn_index % len(
            self.get_parent().get_submenu()) == self.get_parent().get_submenu().index(
            self)

    def select(self):
        return self

    def draw(self, draw, device, i=0):
        line_y = settings.FONT_SIZE * i + (i * settings.LINE_Y_MARGIN)
        if self.is_selected():
            rec = VerticesBox(0, line_y, device.bounding_box[2] - 4,
                              line_y + settings.FONT_SIZE + settings.LINE_Y_MARGIN)
            draw.rectangle(rec, fill="white")
            draw.text(Position(2, line_y), self.title(), **default_text(), fill="black")
        else:
            draw.text(Position(2, line_y), self.title(), **default_text(), fill="white")
