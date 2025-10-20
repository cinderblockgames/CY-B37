import asyncio
import game
from input import Instance as input
from keep_alive import Instance as keep_alive


class GameRunner:
  async def watch(self):
    while keep_alive.state:
      event = input.next_event()
      if event:
        if event.left and event.right:
          game.current = game.start_reset()
        elif event.left:
          game.current.left()
        elif event.middle:
          game.current.middle()
        elif event.right:
          game.current.right()
      await asyncio.sleep(0.01)


Instance = GameRunner()
