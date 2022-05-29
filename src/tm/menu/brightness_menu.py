from tm.contrib.locale import _
from tm.menu.base import *


class BrightnessMenuItem(MenuListItem):

    def __init__(self, **kwargs):
        kwargs["title"] = _("Brightness")
        super(BrightnessMenuItem, self).__init__(MenuItem(parent=self, title="1hi"), MenuItem(parent=self, title="1b"),
                                                 MenuItem(parent=self, title="1c"),
                                                 BackMenuItem(parent=self),
                                                 **kwargs)
