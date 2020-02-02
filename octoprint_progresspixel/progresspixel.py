from rpi_ws281x import Adafruit_NeoPixel, Color
import sys
import math

LED_FREQ_HZ = 800000
LED_DMA = 10
LED_INVERT = False


def fill(strip, color):
    for x in range(strip.numPixels()):
        strip.setPixelColor(x, color)


def hex_to_rgb(hex):
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))


def mix(color1, color2, weight):
    color1_weighted = tuple(x * weight for x in color1)
    color2_weighted = tuple(x * (1-weight) for x in color2)
    return tuple(int(math.floor(sum(x))) for x in zip(color1_weighted, color2_weighted))


if len(sys.argv) >= 5:
    LED_COUNT = int(sys.argv[1])
    LED_PIN = int(sys.argv[2])
    LED_BRIGHTNESS = int(sys.argv[3])
    if sys.argv[4] == "clear":
        action = "clear"
    else:
        action = "None"
        progress = int(sys.argv[4])
        background_color = hex_to_rgb(str(sys.argv[5]))
        bar_color = hex_to_rgb(str(sys.argv[6]))

else:
    print("not enough arguments")
    sys.exit(1)

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
strip.begin()

if action == "clear":
    color = Color(0, 0, 0)
    fill(strip, color)
else:
    # Update pixels here with progress
    current_progress = progress * (float(LED_COUNT) / 100)
    current_led = int(math.floor(current_progress))
    bar_percentage = math.modf(current_progress)[0]

    current_led_color = mix(bar_color, background_color, bar_percentage)

    fill(strip, Color(*background_color))
    for x in range(current_led):
        strip.setPixelColor(x, Color(*bar_color))
    strip.setPixelColor(current_led, Color(*current_led_color))

strip.show()

print("ok")
