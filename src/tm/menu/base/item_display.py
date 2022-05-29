import logging

from tm.contrib.pos import Direction

log = logging.getLogger()


class ItemDisplay:

    def __init__(self, menu_manager, length=4):
        self.menu_manager = menu_manager
        self._length = length
        self._index_list = list(range(0, length))

    @property
    def length(self):
        return self._length

    def freeze(self):
        pass

    def calc(self):
        selected_index = self.menu_manager.active.get_selected_index()

        def apply_calc(calculations):
            selected_index = self.menu_manager.active.get_selected_index()
            for i, c in enumerate(calculations):
                res_index = selected_index + c
                self._index_list[i] = res_index
            return self._index_list

        # start at 0
        if selected_index <= 0:
            calculations = list(range(0, self.length))
            return apply_calc(calculations)

        if selected_index == 1:
            calculations = list(range(-1, self.length - 1))
            return apply_calc(calculations)

        # start at end
        if selected_index == len(self.menu_manager.active.submenu) - 1:
            calculations = list(range(0 - self.length + 1, 1))
            return apply_calc(calculations)

        if selected_index == len(self.menu_manager.active.submenu) - 2:
            calculations = list(range(-2, self.length - 2))
            return apply_calc(calculations)

        # at the end
        if len(self.menu_manager.active.submenu) - 1 <= selected_index:
            calculations = list(range(0 - self.length + 1, 1))
            return apply_calc(calculations)

        if self.menu_manager.last_orientation == Direction.DOWN:
            calculations = list(range((0 - self.length + 2), 2))
            return apply_calc(calculations)

        if self.menu_manager.last_orientation == Direction.UP:
            calculations = list(range(-1, self._length - 1))
            return apply_calc(calculations)

    def validate_index_list(self):
        if len(self.menu_manager.active.submenu) < self.length:
            assert len(self.menu_manager.active.submenu) == len(self._index_list)
        else:
            assert len(self._index_list) == self.length
        assert len(list(set(self._index_list))) == len(self._index_list)
