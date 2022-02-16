# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2022 Neradoc
# SPDX-License-Identifier: MIT

import board
import time
import wifi
from adafruit_wsgi.wsgi_app import WSGIApp
import wsgiserver as server

############################################################################
############################################################################

import displayio
import terminalio
from adafruit_display_text.bitmap_label import Label

oled = board.DISPLAY
splash = displayio.Group()

main_label = Label(
    text="Connecting...",
    font=terminalio.FONT,
    color=0xFFFFFF,
    scale=2,
    anchored_position=(oled.width // 2, oled.height // 2),
    anchor_point=(0.5, 0.5),
)
splash.append(main_label)
oled.show(splash)

############################################################################
############################################################################

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
wifi.radio.connect(secrets["ssid"], secrets["password"])
HOST = repr(wifi.radio.ipv4_address)
PORT = 80  # Port to listen on
print(HOST, PORT)

############################################################################
############################################################################

# Here we create our application, registering the
# following functions to be called on specific HTTP GET requests routes

web_app = WSGIApp()


@web_app.route("/")
def homepage(request):  # pylint: disable=unused-argument
    text = """
    <h3>Text color</h3>
    <p><a href="/led_off">White</a></p>
    <p><a href="/led_on/255/0/0">RED</a></p>
    <p><a href="/led_on/0/255/0">GREEN</a></p>
    <p><a href="/led_on/0/0/255">BLUE</a></p>
    """
    return ("200 OK", [], text)


@web_app.route("/led_on/<r>/<g>/<b>")
def led_on(request, r, g, b):  # pylint: disable=unused-argument
    print("led on!")
    main_label.color = (int(r), int(g), int(b))
    text = f"""
    <p>Color is {(int(r), int(g), int(b))}.
    <span style="background:rgb{(int(r), int(g), int(b))}; display:inline-block; width: 2em;">&nbsp;</span>
    </p>
    <p><a href="/">Go back</a></p>
    """
    return ("200 OK", [], text)


@web_app.route("/led_off")
def led_off(request):  # pylint: disable=unused-argument
    print("led off!")
    main_label.color = (255, 255, 255)
    text = """
    <p>Color is white.</p>
    <p><a href="/">Go back</a></p>
    """
    return ("200 OK", [], text)


############################################################################
############################################################################

# Here we setup our server, passing in our web_app as the application
wsgiServer = server.WSGIServer(80, application=web_app)

print(f"open this IP in your browser: http://{HOST}:{PORT}/")
main_label.text = f"{HOST}"

# Start the server
wsgiServer.start()
while True:
    # Our main loop where we have the server poll for incoming requests
    wsgiServer.update_poll()
    # Could do any other background tasks here, like reading sensors
    time.sleep(0.01)
