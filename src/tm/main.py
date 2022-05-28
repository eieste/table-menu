import argparse
import logging

import RPi.GPIO as GPIO
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106

from tm.menu.menumanager import MenuManager, Direction

log = logging.getLogger()

GPIO.setmode(GPIO.BOARD)


def get_parser():
    parser = argparse.ArgumentParser()
    return parser


def add_arguments(parser: argparse.ArgumentParser):
    parser.add_argument("-d", "--debug", action="store_true", help="Debug flag")
    parser.add_argument("--start", action="store_true", help="Start Menu Manager")
    return parser


def handle_default_options(options):
    if options.debug:
        log.setLevel(logging.DEBUG)
    if options.start:
        start()


def start():
    menu_manager = MenuManager()

    # Hier werden die Eingangs-Pins deklariert, an dem der Sensor angeschlossen ist.
    PIN_CLK = 15
    PIN_DT = 13
    BUTTON_PIN = 11

    GPIO.setup(PIN_CLK, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(PIN_DT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # Benötigte Variablen werden initialisiert
    Counter = 0
    Richtung = True
    PIN_CLK_LETZTER = 0
    PIN_CLK_AKTUELL = 0

    # Initiales Auslesen des Pin_CLK
    PIN_CLK_LETZTER = GPIO.input(PIN_CLK)

    # Diese AusgabeFunktion wird bei Signaldetektion ausgefuehrt
    def ausgabeFunktion(null):
        PIN_CLK_AKTUELL = GPIO.input(PIN_CLK)
        if PIN_CLK_AKTUELL != PIN_CLK_LETZTER:

            if GPIO.input(PIN_DT) != PIN_CLK_AKTUELL:
                menu_manager.update(Direction.UP)
            else:
                menu_manager.update(Direction.DOWN)

    def CounterReset(null):
        menu_manager.reset_switch()

    GPIO.add_event_detect(PIN_CLK, GPIO.BOTH, callback=ausgabeFunktion, bouncetime=100)
    GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=CounterReset, bouncetime=100)

    # device = pygame()

    # substitute bitbang_6800(RS=7, E=8, PINS=[25,24,23,27]) below if using that interface
    serial = i2c(port=1, address=0x3C)

    # substitute ssd1331(...) or sh1106(...) below if using that device
    device = sh1106(serial)

    while True:
        with canvas(device) as draw:
            menu_manager.draw(draw, device)


if __name__ == "__main__":
    parser = get_parser()
    parser = add_arguments(parser)
    options = parser.parse_args()
    handle_default_options(options)
