import games.reset
import games.spike
import games.shift
import games.hintaro
import games.music
import games.settings

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

def start_music():
  return start(games.music)

def start_settings():
  return start(games.settings)

current = start_reset()
