#!/usr/bin/env python
import RPi.GPIO as GPIO
import time


buzzer = None

def setup():
  global buzzer
  buzzer = CuteBuzzerSounds(16)


# https://peppe8o.com/use-passive-buzzer-with-raspberry-pi-and-python/

class CuteBuzzerSounds:
  def __init__(self, pin, dutycycle=50): # dutycycle = volume, 0-50
    self.trigger = pin
    self.dutycycle = dutycycle

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.trigger, GPIO.OUT)

    self.buzzer = GPIO.PWM(self.trigger, 1000) # Dummy frequency.

  def sleep(self, duration):
    durationSeconds = duration / 1000
    time.sleep(durationSeconds)

  def tone(self, frequency, duration, silentDuration):
    if silentDuration == 0:
      silentDuration = 1

    # These come in as ms.
    durationSeconds = duration / 1000
    silentDurationSeconds = silentDuration / 1000

    if frequency > 0:
      self.buzzer.ChangeFrequency(frequency)
      self.buzzer.start(self.dutycycle)
    time.sleep(durationSeconds)
    self.buzzer.stop()
    time.sleep(silentDurationSeconds)

  def bendTones(self, initFrequency, finalFrequency, prop, noteDuration, silentDuration):
    if silentDuration == 0:
      silentDuration = 1

    frequency = initFrequency
    if initFrequency < finalFrequency:
      while frequency < finalFrequency:
        self.tone(frequency, noteDuration, silentDuration)
        frequency = frequency * prop
    else:
      while frequency > finalFrequency:
        self.tone(frequency, noteDuration, silentDuration)
        frequency = frequency / prop

  def play(self, sounds):
    for sound in sounds:
      if len(sound) == 1:
        self.sleep(*sound)
      elif len(sound) == 3:
        self.tone(*sound)
      elif len(sound) == 5:
        self.bendTones(*sound)

  def playSong(self, song):
    index = 0
    max = len(song.notes)
    while index < max:
      self.play([
        [ song.notes[index], song.durations[index] * song.speedMultiplier, 0 ]
      ])
      index = index + 1


# https://github.com/GypsyRobot/CuteBuzzerSounds/

class Notes:
  C0  = 16.35   # C0
  Db0 = 17.32   # C#0/Db0
  D0  = 18.35   # D0
  Eb0 = 19.45   # D#0/Eb0
  E0  = 20.6    # E0
  F0  = 21.83   # F0
  Gb0 = 23.12   # F#0/Gb0
  G0  = 24.5    # G0
  Ab0 = 25.96   # G#0/Ab0
  A0  = 27.5    # A0
  Bb0 = 29.14   # A#0/Bb0
  B0  = 30.87   # B0
  C1  = 32.7    # C1
  Db1 = 34.65   # C#1/Db1
  D1  = 36.71   # D1
  Eb1 = 38.89   # D#1/Eb1
  E1  = 41.2    # E1
  F1  = 43.65   # F1
  Gb1 = 46.25   # F#1/Gb1
  G1  = 49      # G1
  Ab1 = 51.91   # G#1/Ab1
  A1  = 55      # A1
  Bb1 = 58.27   # A#1/Bb1
  B1  = 61.74   # B1
  C2  = 65.41   # C2 (Middle C)
  Db2 = 69.3    # C#2/Db2
  D2  = 73.42   # D2
  Eb2 = 77.78   # D#2/Eb2
  E2  = 82.41   # E2
  F2  = 87.31   # F2
  Gb2 = 92.5    # F#2/Gb2
  G2  = 98      # G2
  Ab2 = 103.83  # G#2/Ab2
  A2  = 110     # A2
  Bb2 = 116.54  # A#2/Bb2
  B2  = 123.47  # B2
  C3  = 130.81  # C3
  Db3 = 138.59  # C#3/Db3
  D3  = 146.83  # D3
  Eb3 = 155.56  # D#3/Eb3
  E3  = 164.81  # E3
  F3  = 174.61  # F3
  Gb3 = 185     # F#3/Gb3
  G3  = 196     # G3
  Ab3 = 207.65  # G#3/Ab3
  A3  = 220     # A3
  Bb3 = 233.08  # A#3/Bb3
  B3  = 246.94  # B3
  C4  = 261.63  # C4
  Db4 = 277.18  # C#4/Db4
  D4  = 293.66  # D4
  Eb4 = 311.13  # D#4/Eb4
  E4  = 329.63  # E4
  F4  = 349.23  # F4
  Gb4 = 369.99  # F#4/Gb4
  G4  = 392     # G4
  Ab4 = 415.3   # G#4/Ab4
  A4  = 440     # A4
  Bb4 = 466.16  # A#4/Bb4
  B4  = 493.88  # B4
  C5  = 523.25  # C5
  Db5 = 554.37  # C#5/Db5
  D5  = 587.33  # D5
  Eb5 = 622.25  # D#5/Eb5
  E5  = 659.26  # E5
  F5  = 698.46  # F5
  Gb5 = 739.99  # F#5/Gb5
  G5  = 783.99  # G5
  Ab5 = 830.61  # G#5/Ab5
  A5  = 880     # A5
  Bb5 = 932.33  # A#5/Bb5
  B5  = 987.77  # B5
  C6  = 1046.5  # C6
  Db6 = 1108.73 # C#6/Db6
  D6  = 1174.66 # D6
  Eb6 = 1244.51 # D#6/Eb6
  E6  = 1318.51 # E6
  F6  = 1396.91 # F6
  Gb6 = 1479.98 # F#6/Gb6
  G6  = 1567.98 # G6
  Ab6 = 1661.22 # G#6/Ab6
  A6  = 1760    # A6
  Bb6 = 1864.66 # A#6/Bb6
  B6  = 1975.53 # B6
  C7  = 2093    # C7
  Db7 = 2217.46 # C#7/Db7
  D7  = 2349.32 # D7
  Eb7 = 2489.02 # D#7/Eb7
  E7  = 2637.02 # E7
  F7  = 2793.83 # F7
  Gb7 = 2959.96 # F#7/Gb7
  G7  = 3135.96 # G7
  Ab7 = 3322.44 # G#7/Ab7
  A7  = 3520    # A7
  Bb7 = 3729.31 # A#7/Bb7
  B7  = 3951.07 # B7
  C8  = 4186.01 # C8
  Db8 = 4434.92 # C#8/Db8
  D8  = 4698.64 # D8
  Eb8 = 4978.03 # D#8/Eb8

class Song:
  def __init__(self, notes, durations, speed):
    self.notes = notes
    self.durations = durations
    self.speedMultiplier = 1.0 / speed

class Songs:
  pirates = Song(
    [
      Notes.E4, Notes.G4, Notes.A4, Notes.A4, 0,
      Notes.A4, Notes.B4, Notes.C5, Notes.C5, 0,
      Notes.C5, Notes.D5, Notes.B4, Notes.B4, 0,
      Notes.A4, Notes.G4, Notes.A4, 0,

      Notes.E4, Notes.G4, Notes.A4, Notes.A4, 0,
      Notes.A4, Notes.B4, Notes.C5, Notes.C5, 0,
      Notes.C5, Notes.D5, Notes.B4, Notes.B4, 0,
      Notes.A4, Notes.G4, Notes.A4, 0,

      Notes.E4, Notes.G4, Notes.A4, Notes.A4, 0,
      Notes.A4, Notes.C5, Notes.D5, Notes.D5, 0,
      Notes.D5, Notes.E5, Notes.F5, Notes.F5, 0,
      Notes.E5, Notes.D5, Notes.E5, Notes.A4, 0,

      Notes.A4, Notes.B4, Notes.C5, Notes.C5, 0,
      Notes.D5, Notes.E5, Notes.A4, 0,
      Notes.A4, Notes.C5, Notes.B4, Notes.B4, 0,
      Notes.C5, Notes.A4, Notes.B4, 0,

      Notes.A4, Notes.A4,
      # Repeat of first part
      Notes.A4, Notes.B4, Notes.C5, Notes.C5, 0,
      Notes.C5, Notes.D5, Notes.B4, Notes.B4, 0,
      Notes.A4, Notes.G4, Notes.A4, 0,

      Notes.E4, Notes.G4, Notes.A4, Notes.A4, 0,
      Notes.A4, Notes.B4, Notes.C5, Notes.C5, 0,
      Notes.C5, Notes.D5, Notes.B4, Notes.B4, 0,
      Notes.A4, Notes.G4, Notes.A4, 0,

      Notes.E4, Notes.G4, Notes.A4, Notes.A4, 0,
      Notes.A4, Notes.C5, Notes.D5, Notes.D5, 0,
      Notes.D5, Notes.E5, Notes.F5, Notes.F5, 0,
      Notes.E5, Notes.D5, Notes.E5, Notes.A4, 0,

      Notes.A4, Notes.B4, Notes.C5, Notes.C5, 0,
      Notes.D5, Notes.E5, Notes.A4, 0,
      Notes.A4, Notes.C5, Notes.B4, Notes.B4, 0,
      Notes.C5, Notes.A4, Notes.B4, 0,
      # End of Repeat

      Notes.E5, 0, 0, Notes.F5, 0, 0,
      Notes.E5, Notes.E5, 0, Notes.G5, 0, Notes.E5, Notes.D5, 0, 0,
      Notes.D5, 0, 0, Notes.C5, 0, 0,
      Notes.B4, Notes.C5, 0, Notes.B4, 0, Notes.A4,

      Notes.E5, 0, 0, Notes.F5, 0, 0,
      Notes.E5, Notes.E5, 0, Notes.G5, 0, Notes.E5, Notes.D5, 0, 0,
      Notes.D5, 0, 0, Notes.C5, 0, 0,
      Notes.B4, Notes.C5, 0, Notes.B4, 0, Notes.A4
    ],
    [
      125, 125, 250, 125, 125,
      125, 125, 250, 125, 125,
      125, 125, 250, 125, 125,
      125, 125, 375, 125,

      125, 125, 250, 125, 125,
      125, 125, 250, 125, 125,
      125, 125, 250, 125, 125,
      125, 125, 375, 125,

      125, 125, 250, 125, 125,
      125, 125, 250, 125, 125,
      125, 125, 250, 125, 125,
      125, 125, 125, 250, 125,

      125, 125, 250, 125, 125,
      250, 125, 250, 125,
      125, 125, 250, 125, 125,
      125, 125, 375, 375,

      250, 125,
      #Repeat of First Part
      125, 125, 250, 125, 125,
      125, 125, 250, 125, 125,
      125, 125, 375, 125,

      125, 125, 250, 125, 125,
      125, 125, 250, 125, 125,
      125, 125, 250, 125, 125,
      125, 125, 375, 125,

      125, 125, 250, 125, 125,
      125, 125, 250, 125, 125,
      125, 125, 250, 125, 125,
      125, 125, 125, 250, 125,

      125, 125, 250, 125, 125,
      250, 125, 250, 125,
      125, 125, 250, 125, 125,
      125, 125, 375, 375,
      # End of Repeat

      250, 125, 375, 250, 125, 375,
      125, 125, 125, 125, 125, 125, 125, 125, 375,
      250, 125, 375, 250, 125, 375,
      125, 125, 125, 125, 125, 500,

      250, 125, 375, 250, 125, 375,
      125, 125, 125, 125, 125, 125, 125, 125, 375,
      250, 125, 375, 250, 125, 375,
      125, 125, 125, 125, 125, 500
    ],
    1.0
  )

  black_parade = Song(
    [
      Notes.G4, Notes.F4, Notes.B5,
      Notes.E4, Notes.D4, Notes.G4,
      Notes.C4, Notes.B4, Notes.E4,
      Notes.A4, Notes.D4
    ],
    [
      250, 125, 125,
      250, 125, 125,
      250, 125, 125,
      250, 187.5
    ],
    0.2
  )

class Sounds:
  connection = [
    [Notes.E5, 50, 30],
    [Notes.E6, 55, 25],
    [Notes.A6, 60, 10]
   ]

  disconnection = [
    [Notes.E5, 50, 30],
    [Notes.A6, 55, 25],
    [Notes.E6, 50, 60]
  ]

  button_pushed = [
    [Notes.E6, Notes.G6, 1.03, 20, 2],
    [30],
    [Notes.E6, Notes.D7, 1.04, 10, 2]
  ]

  mode_1 = [
    [Notes.E6, Notes.A6, 1.02, 30, 10]
  ]

  mode_2 = [
    [Notes.G6, Notes.D7, 1.03, 30, 10]
  ]

  mode_3 = [
    [Notes.E6, 50 , 100],
    [Notes.G6, 50 ,  80],
    [Notes.D7, 300,   0]
  ]

  surprise = [
    [800 , 2150, 1.02, 10, 1],
    [2149, 800 , 1.03, 7 , 1]
  ]

  jump = [
    [880, 2000, 1.04, 8, 3],
    [200]
  ]

  ohooh = [
    [880, 2000, 1.04, 8, 3],
    [200],
    [Notes.B6, 5, 10],
    [Notes.B6, 5, 10],
    [Notes.B6, 5, 10],
    [Notes.B6, 5, 10],
    [Notes.B6, 5, 10],
    [Notes.B6, 5, 10],
    [Notes.B6, 5, 10],
    [Notes.B6, 5, 10],
    [Notes.B6, 5, 10],
    [Notes.B6, 5, 10],
    [Notes.B6, 5, 10],
    [Notes.B6, 5, 10],
    [Notes.B6, 5, 10],
    [Notes.B6, 5, 10],
    [Notes.B6, 5, 10],
    [Notes.B6, 5, 10],
    [Notes.B6, 5, 10],
    [Notes.B6, 5, 10],
    [Notes.B6, 5, 10],
    [Notes.B6, 5, 10],
    [Notes.B6, 5, 10]
  ]

  ohooh2 = [
    [1880, 3000, 1.03, 8, 3],
    [200],
    [Notes.C6, 10, 10],
    [Notes.C6, 10, 10],
    [Notes.C6, 10, 10],
    [Notes.C6, 10, 10],
    [Notes.C6, 10, 10],
    [Notes.C6, 10, 10],
    [Notes.C6, 10, 10],
    [Notes.C6, 10, 10],
    [Notes.C6, 10, 10],
    [Notes.C6, 10, 10],
    [Notes.C6, 10, 10],
    [Notes.C6, 10, 10],
    [Notes.C6, 10, 10],
    [Notes.C6, 10, 10],
    [Notes.C6, 10, 10],
    [Notes.C6, 10, 10]
  ]

  cuddly = [
    [700, 900, 1.03, 16, 4],
    [899, 650, 1.01, 18, 7]
  ]

  sleeping = [
    [100, 500, 1.04, 10, 10],
    [500],
    [400, 100, 1.04, 10, 1 ]
  ]

  happy = [
    [1500, 2500, 1.05, 20, 8],
    [2499, 1500, 1.05, 25, 8]
  ]

  super_happy = [
    [2000, 6000, 1.05, 8 , 3],
    [50],
    [5999, 2000, 1.05, 13, 2]
  ]

  happy_short = [
    [1500, 2000, 1.05, 15, 8],
    [100],
    [1900, 2500, 1.05, 10, 8]
  ]

  sad = [
    [880, 669, 1.02, 20, 200]
  ]

  confused = [
    [1000, 1700, 1.03, 8, 2 ],
    [1699, 500 , 1.04, 8, 3 ],
    [1000, 1700, 1.05, 9, 10]
  ]
