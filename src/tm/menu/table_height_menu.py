from tm.contrib.locale import _
from tm.menu.base.menu_list import MenuListItem


class TableHeightMenuItem(MenuListItem):

    def __init__(self, **kwargs):
        kwargs["title"] = _("Table height")
        super(TableHeightMenuItem, self).__init__(**kwargs)
