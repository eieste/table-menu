from tm.contrib.pos import Direction
import logging
import time


log = logging.getLogger(__name__)

def setup_gpio(menu_manager):
    import RPi.GPIO as GPIO
    # Hier werden die Eingangs-Pins deklariert, an dem der Sensor angeschlossen ist.
    PIN_CLK = 29
    PIN_DT = 31
    BUTTON_PIN = 33
    log.info("Setup GPIO")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIN_CLK, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(PIN_DT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    PIN_CLK_LETZTER = GPIO.input(PIN_CLK)
    PIN_CLK_AKTUELL = 0

    def ausgabeFunktion(null):
        PIN_CLK_AKTUELL = GPIO.input(PIN_CLK)
        if PIN_CLK_AKTUELL != PIN_CLK_LETZTER:
            if GPIO.input(PIN_DT) != PIN_CLK_AKTUELL:
                log.info("Rotary Trigger UP")
                menu_manager.update(Direction.UP)
            else:
                log.info("Rotary Trigger DOWN")
                menu_manager.update(Direction.DOWN)

    def CounterReset(null):
        print("PARTY")
        menu_manager.update(Direction.SELECT)
    log.debug("Register GPIO events")
    GPIO.add_event_detect(PIN_CLK, GPIO.BOTH, callback=ausgabeFunktion, bouncetime=500)
    GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=CounterReset, bouncetime=500)

