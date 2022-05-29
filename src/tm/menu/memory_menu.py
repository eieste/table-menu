from tm.contrib.locale import _
from tm.menu.base import *


class MemoryMenuItem(MenuListItem):

    def __init__(self, **kwargs):
        kwargs["title"] = _("Memory")
        super(MemoryMenuItem, self).__init__(MenuItem(parent=self, title="2hi"), MenuItem(parent=self, title="2b"),
                                             MenuItem(parent=self, title="2c"),
                                             BackMenuItem(parent=self), **kwargs)
