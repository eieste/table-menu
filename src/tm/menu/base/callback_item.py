from tm.menu.base.generic_item import MenuItem


class CallbackMenuItem(MenuItem):

    def __init__(self, **kwargs):
        self._callback = kwargs.pop("callback")
        super(CallbackMenuItem, self).__init__(**kwargs)

    def select(self):
        return self._callback()
