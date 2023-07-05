import board
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction, Pull
import usb_hid
from adafruit_hid.mouse import Mouse

mouse = Mouse(usb_hid.devices)
xAxis = AnalogIn(board.GP26)
yAxis = AnalogIn(board.GP27)
button = DigitalInOut(board.GP16)
button.direction = Direction.INPUT
button.pull = Pull.UP

in_min, in_max, out_min, out_max = (0, 65000, -5, 5)
filter_joystick_deadzone = lambda x: int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min) if abs(x - 32768) > 30000 else 0
cubic_map = lambda x: x**3 / (out_max**2)


while True:
    x_offset = int(cubic_map(filter_joystick_deadzone(xAxis.value)))
    y_offset = int(cubic_map(filter_joystick_deadzone(yAxis.value)))
    mouse.move(x_offset, y_offset, 0)
    if not button.value:
        mouse.click(Mouse.LEFT_BUTTON)