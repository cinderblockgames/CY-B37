#!/usr/bin/env python
import asyncio
from evdev import InputDevice, categorize, ecodes
from pathlib import Path
from time import sleep
from keep_alive import Instance as keep_alive


INPUT_PATH = "/dev/input/event2"

LEFT = 2
MIDDLE = 3
RIGHT = 4

PRESSED = 1
RELEASED = 0


class KeysInputEvent:
  def __init__(self):
    self.left = False
    self.middle = False
    self.right = False

  def __repr__(self):
    return f"<KeysInputEvent left={self.left} middle={self.middle} right={self.right}>"


class InputQueue:
  def __init__(self):
    print("Waiting for keypad to connect...")
    input_path = Path(INPUT_PATH)
    while not input_path.exists():
      pass
    sleep(0.2)  # give file time to get permissions established

    print("Keypad connected!")
    self.keys = InputDevice(INPUT_PATH)
    self.queue = []
    self.current = None

  def press(self, key):
    if not self.current:
      self.current = KeysInputEvent()

    if key == LEFT:
      self.current.left = True
    elif key == MIDDLE:
      self.current.middle = True
    elif key == RIGHT:
      self.current.right = True

  def release(self, key):
    if self.current:
      self.queue.append(self.current)
      self.current = None

  def next_event(self):
    if len(self.queue) > 0:
      return self.queue.pop(0)

  async def watch(self):
    while keep_alive.state:
      try:
        event = self.keys.read_one()
        if event and event.type == ecodes.EV_KEY:
          if event.value == PRESSED:
            self.press(event.code)
          elif event.value == RELEASED:
            self.release(event.code)
        await asyncio.sleep(0.01)
      except:
        print("Keypad disconnected; shutting down...")
        # keypad turned off; assume time to shut down
        keep_alive.state = False


Instance = InputQueue()
