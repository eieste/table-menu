import logging

from tm.menu.base.menu_list import MenuListItem
from tm.menu.brightness_menu import BrightnessMenuItem
from tm.menu.mama import MamaMenuItem
from tm.menu.memory_menu import MemoryMenuItem
from tm.menu.metric_height_menu import MetricHeightMenuItem
from tm.menu.table_height_menu import TableHeightMenuItem

log = logging.getLogger()


class MainMenu(MenuListItem):

    def __init__(self, **kwargs):
        self._menu_manager = kwargs.pop("menu_manager")
        menu_item_list = [
            BrightnessMenuItem(parent=self),
            MemoryMenuItem(parent=self),
            MetricHeightMenuItem(parent=self),
            TableHeightMenuItem(parent=self),
            MamaMenuItem(parent=self)
        ]
        kwargs["title"] = "TableMenu"
        kwargs["parent"] = self
        super(MainMenu, self).__init__(*menu_item_list, **kwargs)

    def get_menu_manager(self):
        return self._menu_manager

    def draw(self, draw, device, i=0):
        self.draw_as_parent(draw, device)
