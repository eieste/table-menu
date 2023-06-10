from tm.contrib.locale import _
from tm.menu.base import *


class MamaMenuItem(MenuListItem):

    def __init__(self, **kwargs):
        kwargs["title"] = _("Hallo Mama")
        super(MamaMenuItem, self).__init__(MenuItem(parent=self, title="Schlafen"),
                                           MenuItem(parent=self, title="Essen"),
                                           MenuItem(parent=self, title="Party!!!!"),
                                           BackMenuItem(parent=self),
                                           **kwargs)
