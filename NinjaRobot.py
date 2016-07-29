# coding=utf-8

import threading

from NinjaController import *
from NinjaMemory import *
from NinjaHeart import *

# ----------------------------------------------------------------------------------------------------
class NinjaRobot(object):
    def __init__(self):
        self.controller = NinjaController(self)
        self.controller_thread = threading.Thread(target=self.controller.process)
        self.controller_thread.setDaemon(True)
        self.memory = NinjaMemory(self)
        self.memory_thread = threading.Thread(target=self.memory.process)
        self.memory_thread.setDaemon(True)
        self.heart = NinjaHeart(self)
        self.heart_thread = threading.Thread(target=self.heart.process)
        self.heart_thread.setDaemon(True)

        self.controller.addObserver(self)
        pass

    # ----------------------------------------------------------------------------------------------------
    def run(self):
        self.controller_thread.start()
        self.memory_thread.start()
        self.heart_thread.start()
        while 1:
            time.sleep(9999)
            pass

    # ----------------------------------------------------------------------------------------------------
    def onKeyInput(self, char):
        if char == '\x03':
            print("exit")
            exit(0)
            return True
        return False
