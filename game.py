import games.reset
import games.spike
import games.shift
import games.hintaro

def start(target):
  obj = target.Game()
  obj.start()
  return obj

def start_reset():
  return start(games.reset)

def start_spike():
  return start(games.spike)

def start_shift():
  return start(games.shift)

def start_hintaro():
  return start(games.hintaro)

current = start_reset()
