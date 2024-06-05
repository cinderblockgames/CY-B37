import os

_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'settings')
_settings = {
    'subtitles': os.path.exists(os.path.join(_dir, 'subtitles'))
  }

def toggle_setting(name):
  if _settings[name]:
    _settings[name] = False
    os.remove(os.path.join(_dir, name))
  else:
    _settings[name] = True
    file = open(os.path.join(_dir, name), 'w')
    file.close()

def is_set(name):
  return _settings[name]
