from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106, ssd1306, ssd1325, ssd1331

serial = i2c(port=1, address=0x3c)
device = sh1106(serial)
#device = ssd1306(serial)
#device = ssd1325(serial)
#device = ssd1331(serial)


for y in range(0, 64):
    print(y)
    for x in range(0, 128):
        print(x)
        with canvas(device) as draw:
            draw.rectangle((x, y, x + 50, 50), fill="white")
