This is a quick and dirty port of `adafruit_esp32spi/adafruit_esp32spi_wsgiserver.py` to ESP32-S2.

Tested on a FeatherS2. Will work more on it later unless somebody else wants to use it to start a legitimate library, cookie-cutter and all that.

To run:

- copy all the files to the FeatherS2
- create the usual secrets.py
- install the requirements with circup or manually
- rename `wsgi_simpletest.py` to `code.py`

Test with:

```bash
$ curl http://IP_ADDRESS/led_on/255/255/0
$ curl http://IP_ADDRESS/led_on/255/0/255
$ curl http://IP_ADDRESS/led_off
```

### For support/questions on this library
Please prefer the [Adafruit discord](http://adafru.it/discord), #help-with-circuitpython channel. Your issue might have solutions that other people can help with. Feel free to tag me (@Neradoc), but please no private messages.
