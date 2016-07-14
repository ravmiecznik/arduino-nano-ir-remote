__author__ = 'rafal'

import subprocess
import serial
import remote_comands
import time

class Remote():

    def __init__(self):
        self.device = self._serial_connection('/dev/ttyUSB0', 9600)
        self.current_desk = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.device.close()

    def _serial_connection(self, p, b):
        return serial.Serial(port=p, baudrate=b)

    def xdotool_change_desktop(self, key):
        current_desk = self.current_desk
        if not current_desk:
            current_desk = subprocess.call(["xdotool", "get_desktop"])
        if 'right' in key and current_desk<5:
            current_desk += 1
        if 'left' in key and current_desk>0:
            current_desk -= 1
        if 'down' in key and current_desk<=2:
            current_desk += 3
        if 'up' in key and current_desk>=3:
            current_desk -= 3
        self.current_desk = current_desk
        return ["xdotool", "set_desktop", str(current_desk)]

    def key_handler(self, key):
        if 'arrow' in key:
            action = self.xdotool_change_desktop(key)
            return action
        return None

    def listen(self):
        cmd = None
        while cmd != 'quit':
            code = self.device.readline()
            key = remote_comands.remote_key(code)
            if key:
                print key
                action = self.key_handler(key)
                if action:
                    #print action
                    subprocess.call(action)

R = Remote()
R.listen()



