""" Dog door - initial version

Author: m1ge7
Date: 2014/04/07
"""


class DogDoor:
    
    def __init__(self):
        self._open = False

    def open(self):
        print("The dog door opens")
        self._open = True

    def close(self):
        print("The dog door closes")
        self._open = False

    def is_open(self):
        return self._open


class Remote:

    def __init__(self, door):
        self._door = door

    def press_button(self):
        print("Pressing the remote control button...")
        if self._door.is_open():
            self._door.close()
        else:
            self._door.open()


if __name__ == '__main__':
    door = DogDoor()
    remote = Remote(door)

    print("Fido barks to go outside...")
    remote.press_button()

    print("\nFido has gone outside...")
    remote.press_button()

    print("\nFido's all done...")
    remote.press_button()

    print("\nFido's back inside...")
    remote.press_button()
