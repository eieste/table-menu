import argparse
import logging
import time

from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.emulator.device import pygame
from luma.oled.device import sh1106

from tm.ctl.gpio import setup_gpio
from tm.ctl.input import setup_input
from tm.menu.menu_manager import MenuManager

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
        device = pygame()
        setup_input(menu_manager)
    else:
        serial = i2c(port=1, address=0x3C)
        device = sh1106(serial)
        setup_gpio(menu_manager)

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
