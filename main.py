import random
import time
from blinkstick import blinkstick
import colorsys

h = 0.0
s = 1.0
v = 1.0
max = 8

bs = blinkstick.find_first()
bs.set_led_count(2)

try:
    while True:
        for led in range(2):

            h += 0.025
            # s -= 0.005
            # v -= 0.002

            h %= 1.0
            # s %= 1.0
            # v %= 1.0

            rgb = colorsys.hsv_to_rgb(h, s, v)
            # r = random.randint(0, max)
            # g = random.randint(0, max)
            # b = random.randint(0, max)

            r = int(rgb[0] * max)
            g = int(rgb[1] * max)
            b = int(rgb[2] * max)

            print("h = %s, s = %s, v = %s, r = %s, b = %s, g = %s" % (h, s, v, r, g, b))
            bs.set_color(channel=0, index=led, red=r, green=g, blue=b)
            time.sleep(0.1)
            bs.set_color(channel=0, index=led, red=0, green=0, blue=0)
            time.sleep(0.1)

except KeyboardInterrupt:
    for led in range(2):
        bs.set_color(channel=0, index=led, red=0, green=0, blue=0)
bs.turn_off()
