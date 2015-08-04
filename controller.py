import RPi.GPIO as GPIO

pins = []
pins = [12,16,18,22,32,36,38,40] # Initialize solenoid control pins

class melody_class:
   def __init__(self):
      self.notes = ""
   def add_note(self,addednote):
      self.notes=self.notes+addednote

class controller:
   def __init__(self,initialvelocity,initialspeed):
      # Velocity controls the sustain of each solenoid, between .05 and .2
      self.velocity=initialvelocity
      # Speed controls the time between each hit, between .1 and 1
      self.speed=initialspeed # S
      self.melody = melody_class()
      self.tones = []
      self.rings = []
      self.tones = ['c','d','e','f','g','a','b','C']

      self.rings = []
      self.tones = ['c','d','e','f','g','a','b','C']
      self.rings = ['default','onenote','silence']
      GPIO.setmode(GPIO.BOARD)
      for x in pins:
         GPIO.setup(x,GPIO.OUT) # Setup the GPIO pins as outputs

   # Write a note sequence to be played with self.play()
   def write_sequence(self,fullmelody):
      self.melody.notes = ""
      for x in fullmelody:
         self.melody.add_note(x)
   # Run a test sequence
   def reset(self,inittone):
      if inittone=="default":
         self.write_sequence("cdg")
      if inittone=="onenote":
         self.write_sequence("a")
      if inittone=="silence":
         self.write_sequence("")
   def lift(self,pini):
      # Set a GPIO pin low, turning the soilenoid off
      GPIO.output(pins[pini],GPIO.LOW)
      print("lifted ",pini)
   def hit(self,pinid):
      # Create a new thread, so the notes can be played independently
      t=threading.Timer(self.velocity,self.lift,[pinid])
      t.start()
      # Set a GPIO pin high, turning the soilenoid off
      GPIO.output(pins[pinid],GPIO.HIGH)
      print("hit ",pinid)
   def testtone(self,tested):
      for y in range(0,7):
         if self.tones[y] == tested:
            self.hit(y) #lol python why are you hitting yourself
            break
   def play(self):
      for x in range(len(self.melody.notes)):
         for y in range(0,7):
            if self.tones[y] == self.melody.notes[x]:
               # Create a new thread, so the notes can be played independently
               t=threading.Timer(self.speed*x,self.hit,[y])
               t.start()
               break
   def test(self):
      self.write_sequence("cdefgab")
      self.play()
