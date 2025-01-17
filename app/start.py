from machine import Pin
from time import ticks_ms, sleep_ms

pin = Pin(33, Pin.IN, None)

lastUpdate = 0
lastValue = 0
while True:
    v = pin.value()
    if ticks_ms() > lastUpdate + 3000:
        print(v)
        import app.lightclient as client
        client.setState('on' if v==1 else 'off')
        lastUpdate = ticks_ms()
    elif lastValue != v:
        lastUpdate = ticks_ms()
        lastValue = v
        print(f'debug: updated to {v}@{ticks_ms()}')
    sleep_ms(20)
