import board
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction, Pull
import usb_hid
from adafruit_hid.mouse import Mouse

mouse = Mouse(usb_hid.devices)
xAxis = AnalogIn(board.A1)
yAxis = AnalogIn(board.A0)
button = DigitalInOut(board.GP16)
button.direction = Direction.INPUT
button.pull = Pull.UP

in_min,in_max,out_min,out_max = (0, 65000, -5, 5)
filter_joystick_deadzone = lambda x: int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min) if abs(x - 32768) > 500 else 0


while True:
    x_offset = filter_joystick_deadzone(xAxis.value) * -1 #Invert axis
    y_offset = filter_joystick_deadzone(yAxis.value)
    mouse.move(x_offset, y_offset, 0)
    if not button.value:
        mouse.click(Mouse.LEFT_BUTTON)
