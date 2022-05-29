from tm.contrib.locale import _
from tm.menu.base.callback_item import CallbackMenuItem


class BackMenuItem(CallbackMenuItem):

    def __init__(self, **kwargs):
        kwargs["title"] = _("Zurück")
        kwargs["callback"] = self.goto_parent_menu
        super(BackMenuItem, self).__init__(**kwargs)

    def goto_parent_menu(self):
        self.get_menu_manager().goto(self.get_parent().get_parent())
