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
