#!/usr/bin/env python
import asyncio
from signal import SIGINT, signal
from subprocess import run
from sys import exit
from time import sleep
from traceback import format_exception

from game_runner import Instance as game_runner
from input import Instance as input
import screens


async def main():
  loop = asyncio.get_running_loop()
  loop.add_signal_handler(SIGINT, lambda: turn_off())  # interrupt

  await asyncio.gather(
    game_runner.watch(),
    input.watch(),
    screens.watch(),
  )


def turn_off(*args, exc=None):
  if exc:
    print(type(exc))
    print("".join(format_exception(type(exc), exc, exc.__traceback__)))
  screens.clear()
  screens.write_text('cy-b37', screens.fonts.get_regular_font(64), (10, 80))
  screens.write_text('casino table droid', screens.fonts.get_regular_font(21), (8, 160))
  screens.set_subtitle_generator(lambda: "cy-b37 casino table droid")
  screens.show(force=True)
  sleep(0.2)
  print("Thanks for playing!")
  run(["sudo", "shutdown", "now"], shell=False)  # safely shut down the droid
signal(SIGINT, turn_off)  # interrupt


try:
  asyncio.run(main())
  turn_off()
except Exception as ex:
  turn_off(exc=ex)  # exception
