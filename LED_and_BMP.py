#!/usr/bin/python

#...........................................................................
# Author:  Sumaiya Sabir Mohamed
# Github:  https://github.com/TechnicalVillager
#...........................................................................

# Import Necessary Packages
import Adafruit_BMP.BMP085 as BMP085
import time
import neopixel, board


# BMP085 Barometric Pressure Sensor
sensor = BMP085.BMP085()
initial_altitude = 0

# Mean averaging the initial altitude with 50 samples in the interval
# 0.1 seconds
for x in range (50):
        initial_altitude += sensor.read_altitude()
        time.sleep(0.1)
initial_altitude = initial_altitude/50

print ("Initialization Complete!!!")

# Initializing the LED strip
pixels = neopixel.NeoPixel(board.D18, 55, brightness = 0.8)
pixels.fill((0, 0, 0))

# For indefinite loop adding while True
while True:
        value = 0

        # Mean averaging the initial altitude with 50 samples in the interval
        # 0.01 seconds
        for x in range (50):
                value += sensor.read_altitude() - initial_altitude
                time.sleep(0.01)
        value = value/50
        print(value)

        # Based on the offsets, setting the color of the RGB LED strip to Red,
        # Green and Blue respectively
        if value <= 0.7:
                pixels.fill((255, 0, 0))
        elif value > 0.7 and value <= 1.25:
                pixels.fill((0, 255, 0))
        else:
                pixels.fill((0, 0, 255))
        time.sleep(0.5)