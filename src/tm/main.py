import argparse
import logging
import time

from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106

from tm.config import settings
from tm.ctl.gpio import setup_gpio
from tm.ctl.input import setup_input
from tm.menu.menu_manager import MenuManager
import _thread
log = logging.getLogger()


def get_parser():
    parser = argparse.ArgumentParser()
    return parser


def add_arguments(parser: argparse.ArgumentParser):
    parser.add_argument("-d", "--debug", action="store_true", help="Debug flag")
    parser.add_argument("-e", "--emulator", action="store_true", help="Emulator Flag")
    parser.add_argument("--start", action="store_true", help="Start Menu Manager")
    parser.add_argument("--fps", action="store_true", help="Show FPS")
    parser.add_argument("--slow-render", type=int, choices=range(1, 10), help="Slow down Rendering (in seconds)")
    return parser


def handle_default_options(options):
    if options.debug:
        log.setLevel(logging.DEBUG)
        logging.basicConfig(level=logging.DEBUG)
    if options.start:
        start(options)


def start(options):
    menu_manager = MenuManager(options)

    if options.emulator:
        from luma.emulator.device import pygame
        device = pygame()
        setup_input(menu_manager)
        # simulate_height_sensor()
    else:
        serial = i2c(port=settings.I2C_DISPLAY_PORT, address=settings.I2C_DISPLAY_ID)
        #         SSD1306, SSD1309, SSD1322, SSD1325, SSD1327, SSD1331, SSD1351, SSD1362 and SH1106
        device = sh1106(serial)
        _thread.start_new_thread(setup_gpio, (menu_manager,))
        # setup_height_sensor()
    while True:
        with canvas(device) as draw:
            menu_manager.draw(draw, device)

        if options.slow_render:
            time.sleep(options.slow_render)


if __name__ == "__main__":
    parser = get_parser()
    parser = add_arguments(parser)
    options = parser.parse_args()
    handle_default_options(options)
