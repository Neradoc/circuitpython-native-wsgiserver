This is a port of [Server example](https://github.com/adafruit/Adafruit_CircuitPython_ESP32SPI/tree/main/examples/server) from Adafruit ESP32SPI library to ESP32-S2 WROVER.

Should works on any ESP32-S2 **WROVER** module with builtin Neopixel like
* Adafruit Metro ESP32-S2
* Espressif Saola 1
* MuseLab nanoESP32-S2
* Unexpected Maker FeatherS2

WROOM modules seems not have suficient RAM to run this example.

To run:

* copy `esp32s2_wsgiserver.py` file and `static` folder in CIRCUITPY drive
* create the usual `secrets.py`
* copy required libraries in `CIRCUITPY/lib` folder
  * wsgiserver (from this repo)
  * adafruit_wsgi (from [CircuitPython Libraries](https://circuitpython.org/libraries))
  * neopixel (from [CircuitPython Libraries](https://circuitpython.org/libraries))
* rename `esp32s2_wsgiserver.py` to `code.py`
  or
* type  `import esp32s2_wsgiserver.py` in serial console
* open a web browser at the a adress diplayed in serial console

Support also /led_off and /led_on pathes.
