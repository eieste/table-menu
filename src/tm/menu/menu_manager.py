import logging
import time

from tm.config import settings
from tm.contrib.pos import Position, Direction
from tm.menu.base.draw import default_text
from tm.menu.base.generic_item import MenuItem
from tm.menu.main_menu import MainMenu

log = logging.getLogger()


class MenuManager:

    def __init__(self, options):
        self._fps_start = 0
        self._fps = 0
        self._current_fps = 0
        self.options = options
        self._main_menu = MainMenu(menu_manager=self)
        self.turn_index = 0
        self._last_orientation = -1
        self._last_direction = -1
        self.active = self._main_menu
        pass

    @property
    def last_orientation(self):
        return self._last_orientation

    @property
    def last_direction(self):
        return self._last_direction

    def goto(self, menu_item: MenuItem):
        log.debug(menu_item)
        self.active = menu_item
        log.debug(f"Activate Menu: {menu_item.title()}")

    def update(self, direction):
        self._last_direction = direction
        if direction == Direction.UP:
            self.turn_index = self.turn_index - 1
            self._last_orientation = Direction.UP
        if direction == Direction.DOWN:
            self.turn_index = self.turn_index + 1
            self._last_orientation = Direction.DOWN
        if direction == Direction.SELECT:
            self.active.select()
            self.turn_index = 0

    def draw_fps(self, draw, device):
        if time.time() - self._fps_start >= 1:
            self._fps_start = time.time()
            self._current_fps = self._fps
            self._fps = 0
        self._fps = self._fps + 1

    def draw(self, draw, device):
        if self.options.fps:
            self.draw_fps(draw, device)
            draw.text(Position(device.bounding_box[2] - 20, device.bounding_box[3] - settings.FONT_SIZE),
                      f"{self._current_fps}",
                      **default_text())
        self.active.draw(draw, device)

        # draw.rectangle(device.bounding_box, outline="white", fill="black")
        # i = 0
        # active_item_pos = self._c % len(self.ACTIVE)
        # for item in self.ACTIVE:
        #     tx1 = 1
        #     ty1 = i * settings.FONT_SIZE + 1
        #
        #     log.debug(f"Y => {ty1}")
        #     if active_item_pos == i:
        #         x1 = tx1 - 1
        #         y1 = ty1 - 1
        #         x2 = device.bounding_box[2] - 8
        #         y2 = ty1 - 1 + settings.FONT_SIZE
        #         draw.rectangle((x1, y1, x2, y2), fill="white")
        #         draw.text((5, (i * settings.FONT_SIZE) + 2), f"{item.title}", fill="black",
        #                   font=settings.get_font())
        #     else:
        #         draw.text((tx1, ty1), f"{item.title}", fill="white",
        #                   font=settings.get_font())
        #     i = i + 1
