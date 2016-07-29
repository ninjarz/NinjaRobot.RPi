# coding=utf-8

try:
    import RPi.GPIO as GPIO
except:
    pass

from NinjaComponent import *

# ----------------------------------------------------------------------------------------------------
class NinjaMotor(NinjaComponent):
    def __init__(self):
        super(NinjaMotor, self).__init__()
        self.forward_signal_pin = None
        self.backward_signal_pin = None
        self.is_need_update = False
        self.forward_signal = 0
        self.backward_signal = 0
        pass

    def __del__(self):
        if self.forward_signal_pin is not None:
            self.forward_signal_pin.stop()
        if self.backward_signal_pin is not None:
            self.backward_signal_pin.stop()

    # ----------------------------------------------------------------------------------------------------
    def process(self):
        if self.is_need_update:
            self.is_need_update = False
            self.forward_signal_pin.ChangeDutyCycle(self.forward_signal)
            self.backward_signal_pin.ChangeDutyCycle(self.backward_signal)

    # ----------------------------------------------------------------------------------------------------
    def getPinNames(self):
        return [
            "car_motor_forward_signal_pin",
            "car_motor_backward_signal_pin",
        ];

    def setPins(self, pins):
        super(NinjaMotor, self).setPins(pins)
        forward_signal_pin = self.pins["car_motor_forward_signal_pin"]
        backward_signal_pin = self.pins["car_motor_backward_signal_pin"]
        try:
            GPIO.setup(forward_signal_pin, GPIO.OUT)
            self.forward_signal_pin = GPIO.PWM(forward_signal_pin, 50)
            self.forward_signal_pin.ChangeDutyCycle(0)
            self.forward_signal_pin.start(0)
            GPIO.setup(backward_signal_pin, GPIO.OUT)
            self.backward_signal_pin = GPIO.PWM(backward_signal_pin, 50)
            self.backward_signal_pin.ChangeDutyCycle(0)
            self.backward_signal_pin.start(0)
        except:
            pass

    # ----------------------------------------------------------------------------------------------------
    def onKeyInput(self, char):
        if char == 'w':
            self.forward_signal += 15
            if 100 < self.forward_signal:
                self.forward_signal = 100
            self.backward_signal -= 15
            if self.backward_signal < 0:
                self.backward_signal = 0
            print("forward", self.forward_signal, self.backward_signal)
        elif char == 's':
            self.forward_signal -= 15
            if self.forward_signal < 0:
                self.forward_signal = 0
            self.backward_signal += 15
            if 100 < self.backward_signal:
                self.backward_signal = 100
            print("backward", self.forward_signal, self.backward_signal)
        elif char == 'f':
            self.forward_signal = 0
            self.backward_signal = 0
            print("stop")
        else:
            return False
        self.is_need_update = True
        return True