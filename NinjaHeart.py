# coding=utf-8

import time
import RPi.GPIO as GPIO

# ----------------------------------------------------------------------------------------------------
class NinjaHeart(object):
    def __init__(self, robot):
        self.robot = robot
        self.initComponents()

    # ----------------------------------------------------------------------------------------------------
    def process(self):
        while True:
            time.sleep(0.1)
            pass

    # ----------------------------------------------------------------------------------------------------
    def initGPIO(self):
        GPIO.setwarnings(True)
        GPIO.setmode(GPIO.BCM)
        pass

    # ----------------------------------------------------------------------------------------------------
    def initComponents(self):
        pass
