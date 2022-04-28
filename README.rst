Introduction
============

This is a port of `adafruit_esp32spi/adafruit_esp32spi_wsgiserver.py` to ESP32-S2.

* copy `wsgiserver.py` and all the files in `examples/wsgi_simpletest` to the board.
* create the usual secrets.py (`see here <https://learn.adafruit.com/pyportal-titano-weather-station/code-walkthrough-secrets-py>`)
* install the requirements of the demo with circup or manually
  * `adafruit_wsgi` for the web server application helper
  * `adafruit_dotstar` or `neopixel` for the LED demo
* rename `wsgiserver_simpletest.py` to `code.py`

Test by going to http://IP_ADDRESS/led_on/255/255/0 and http://IP_ADDRESS/led_off


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_
or individual libraries can be installed using
`circup <https://github.com/adafruit/circup>`_.

Installing to a Connected CircuitPython Device with Circup
==========================================================

Make sure that you have ``circup`` installed in your Python environment.
Install it with the following command if necessary:

.. code-block:: shell

    pip3 install circup

With ``circup`` installed and your CircuitPython device connected use the
following command to install:

.. code-block:: shell

    circup install wsgiserver

Or the following command to update an existing version:

.. code-block:: shell

    circup update


Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/Neradoc/CircuitPython_wsgiserver/blob/HEAD/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
