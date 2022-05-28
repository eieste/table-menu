import enum

from tm.menu.brightness import get_brightness_menu_title, change_brightness, set_brightness
from tm.menu.menuitem import MenuItem

BRIGHTNESS = MenuItem("Brightness", submenu={
    MenuItem(get_brightness_menu_title, callback=change_brightness),
    MenuItem("OK", callback=set_brightness)
})

METRIC_HEIGHT = MenuItem("Metric height")

TABLE_HEIGHT = MenuItem("Table height")

MEMORY_POSITION = MenuItem("Memory")


class Direction(enum.IntEnum):
    UP = 0
    DOWN = 1


class MenuManager:
    MENU_TREE = MenuItem("Main Menu", submenu={
        BRIGHTNESS,
        METRIC_HEIGHT,
        TABLE_HEIGHT,
        METRIC_HEIGHT
    })
    ACTIVE = MENU_TREE

    def __init__(self):
        self._c = 1
        pass

    def update(self, direction):
        if direction == 0:
            self._c = self._c + 1
        if direction == 1:
            self._c = self._c - 1

    def reset_switch(self):
        pass

    def draw(self, draw, device):

        draw.rectangle(device.bounding_box, outline="white", fill="black")
        i = 0
        for item in self.ACTIVE:
            if self._c % len(self.ACTIVE) == i:
                print(item.title)
                draw.rectangle((5, i * 15 + 5, 100, i * 15 + 15), outline="white")

            draw.text((5, (i * 15) + 5), f"{item.title} {self._c}", fill="white")
            i = i + 1
        print(i)

        pass
