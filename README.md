1. **Connect the joystick module and button to your Raspberry Pi Pico:**
    - Connect the `GND` pin on the joystick module to a `GND` pin on the Pico.
    - Connect the `VCC` pin on the joystick module to a `3V3(OUT)` pin on the Pico.
    - Connect the `VRx` pin on the joystick module to an analog input pin `GP26` on the Pico.
    - Connect the `VRy` pin on the joystick module to another analog input pin `GP27` on the Pico.
    - Connect the `SW` pin on the joystick module to pin `GP16` on the pico.

2. **Install CircuitPython on your Raspberry Pi Pico:**
    - Download the latest version of CircuitPython for the Raspberry Pi Pico from the [CircuitPython website](https://circuitpython.org/board/raspberry_pi_pico/).
    - Connect your Raspberry Pi Pico to your computer using a micro USB cable while holding down the `BOOTSEL` button on the Pico. This will put the Pico in bootloader mode and it should appear as a USB drive named `RPI-RP2`.
    - Drag and drop the CircuitPython `.uf2` file that you downloaded earlier onto the `RPI-RP2` drive. The Pico will automatically restart and install CircuitPython.
    - After installing CircuitPython, the Pico will appear as a USB drive named `CIRCUITPY`.

3. **Install the `adafruit_hid` library on your Raspberry Pi Pico:**
    - Download the latest version of the Adafruit CircuitPython Library Bundle from the [CircuitPython website](https://circuitpython.org/libraries).
    - Unzip the downloaded file and open the resulting folder.
    - Locate the `adafruit_hid` folder inside the `lib` folder.
    - Open the `CIRCUITPY` drive for your Raspberry Pi Pico and locate or create a folder named `lib`.
    - Copy the entire `adafruit_hid` folder from the unzipped Library Bundle into the `lib` folder on your Raspberry Pi Pico.

4. **Save the code to the pico with the same name**

5. **After saving this code to your Raspberry Pi Pico, it will automatically restart and run it.**

Once you have completed these steps, you should be able to control the mouse on your PC using the joystick module connected to your Raspberry Pi Pico and use its button as a left mouse button
