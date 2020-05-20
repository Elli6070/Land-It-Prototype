# 3M Land-It Note Detection
# by: Ebenezer Dadson 2/13/2020

## RPi to VL6180X Wiring
# Pi 3V3 to sensor Vin
# Pi GND to sensor GND
# Pi SCL to sensor SCL
# Pi SDA to sensor SDA


import time

import board
import busio

import adafruit_vl6180x


# Create I2C bus.
i2c = busio.I2C(board.SCL, board.SDA)

# Create sensor instance.
sensor = adafruit_vl6180x.VL6180X(i2c)

def sense():
# Main loop prints the range and lux every second:
    for i in range(50):
        # Read the range in millimeters and print it.
        range_mm = sensor.range
        print('Range: {0}mm'.format(range_mm))
        light_lux = sensor.read_lux(adafruit_vl6180x.ALS_GAIN_1)
        time.sleep(0.1)
    return range_mm, light_lux

def senseDistance():
    range_mm = sensor.range
    print('Range: {0}mm'.format(range_mm))
    return range_mm

