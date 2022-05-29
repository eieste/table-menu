from tm.contrib.locale import _
from tm.menu.base import *


class MetricHeightMenuItem(MenuListItem):

    def __init__(self, **kwargs):
        kwargs["title"] = _("Metric height")
        super(MetricHeightMenuItem, self).__init__(MenuItem(parent=self, title="3hi"),
                                                   MenuItem(parent=self, title="3b"),
                                                   MenuItem(parent=self, title="3c"),
                                                   BackMenuItem(parent=self), **kwargs)
