# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
import busio
from digitalio import DigitalInOut
import socketpool
import time
import wifi

import wsgiserver as server
from adafruit_wsgi.wsgi_app import WSGIApp
import status_led

# Get wifi details and more from a secrets.py file
try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

# This example depends on a WSGI Server to run.
# We are using the wsgi server made for the ESP32

print("ESP32 S2 simple web app test!")

print("Connect wifi")
wifi.radio.connect(secrets['ssid'],secrets['password'])
HOST = repr(wifi.radio.ipv4_address)
PORT = 80        # Port to listen on
print(HOST,PORT)


"""Use below for Most Boards"""
status_light = status_led.get_status_led(brightness=1)

# Here we create our application, registering the
# following functions to be called on specific HTTP GET requests routes

web_app = WSGIApp()

@web_app.route("/led_on/<r>/<g>/<b>")
def led_on(request, r, g, b):  # pylint: disable=unused-argument
    print("led on!")
    status_light.fill((int(r), int(g), int(b)))
    return ("200 OK", [], "led on!")


@web_app.route("/led_off")
def led_off(request):  # pylint: disable=unused-argument
    print("led off!")
    status_light.fill(0)
    return ("200 OK", [], "led off!")


# Here we setup our server, passing in our web_app as the application
wsgiServer = server.WSGIServer(80, application=web_app)

print(f"open this IP in your browser: http://{HOST}:{PORT}/")

# Start the server
wsgiServer.start()
while True:
    # Our main loop where we have the server poll for incoming requests
    wsgiServer.update_poll()
    # Could do any other background tasks here, like reading sensors
    time.sleep(0.01)
