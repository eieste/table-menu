from pathlib import Path

from PIL import ImageFont


class Configuration:
    ROTARY_PIN_CLK = 29
    ROTARY_PIN_DT = 31
    ROTARY_PIN_SW = 33

    ULTRASONIC_TRIGGER = 23
    ULTRASONIC_ECHO = 24

    I2C_DISPLAY_ID = 0x3c
    I2C_DISPLAY_PORT = 1

    PATH_TO_FONT = "assets/RobotoMono-VariableFont_wght.ttf"
    FONT_SIZE = 12
    LINE_Y_MARGIN = 4
    LOCALE_DIR = "locale/"

    def get_font(self):
        font_path = str(Path(__file__).resolve().parent.joinpath(self.PATH_TO_FONT))
        return ImageFont.truetype(font_path, self.FONT_SIZE)


settings = Configuration()
