import logging

from tm.config import settings
from tm.contrib.pos import SimpleBox
from tm.menu.base import *
from tm.menu.base.item_display import ItemDisplay

log = logging.getLogger()


class MenuListItem(MenuItem):

    def __init__(self, *args, **kwargs):
        if len(args) <= 0:
            args = [BackMenuItem(parent=self)]
        self.submenu = args

        super(MenuListItem, self).__init__(**kwargs)

    def get_submenu(self):
        return self.submenu

    def get_selected_index(self):
        for i, item in enumerate(self.get_submenu()):
            if item.is_selected():
                return i

    def scrollbar(self, draw, device, visible_indexes):
        max_line = round(
            device.bounding_box[3] / (settings.FONT_SIZE + settings.LINE_Y_MARGIN))
        visible_items = max_line if len(self.submenu) > max_line else len(self.submenu)
        display_height = device.bounding_box[3]
        item_fraction = len(self.submenu) / visible_items

        if self.get_selected_index() == 0:
            top = 0
        else:
            top = visible_indexes[0] * display_height / len(self.submenu)

        height = display_height / item_fraction

        scroll_bar = SimpleBox(device.bounding_box[2] - 1, top, 1, height)
        draw.rectangle(scroll_bar.get_vertices(), fill="white")

    def draw_as_parent(self, draw, device):
        max_line = round(
            device.bounding_box[3] / (settings.FONT_SIZE + settings.LINE_Y_MARGIN))
        visible_items = ItemDisplay(self.get_menu_manager(),
                                    length=max_line if len(self.submenu) > max_line else len(self.submenu))
        visible_indexes = visible_items.calc()
        pos = 0
        for i in visible_indexes:
            self.submenu[i].draw(draw, device, pos)
            pos = pos + 1
        self.scrollbar(draw, device, visible_indexes)

    def draw(self, draw, device, i=0):
        if self.get_menu_manager().active is self:
            self.draw_as_parent(draw, device)
        else:
            super(MenuListItem, self).draw(draw, device, i)

    def select(self):

        if len(self.submenu) <= 0:
            self.get_menu_manager().goto(self)

        for item in self.submenu:
            if item.is_selected():
                log.debug(f"JUMP TO {item.title()}")
                if isinstance(item, MenuListItem):
                    self.get_menu_manager().goto(item)
                else:
                    item.select()
