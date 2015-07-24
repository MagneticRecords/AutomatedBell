import threading

pins = [1,2,3,4,5,6,7]

class melody_class:
   def __init__(self):
      self.notes = []
   def add_note(self,addednote):
      self.notes.append(addednote)
   
class controller:
   def __init__(self,initialvelocity,initialspeed):
      self.velocity=initialvelocity
      self.speed=initialspeed
      self.melody = melody_class()
      self.tones = []
      self.rings = []
      self.tones = ['c','d','e','f','g','a','b','C']
      self.rings = ['default','onenote','silence']
   def write_sequence(self,fullmelody):
      self.melody.notes = ""
      for x in fullmelody:
         self.melody.add_note(x)
   def reset(self,inittone):
      if inittone=="default":
         self.write_sequence("cdg")
      if inittone=="onenote":
         self.write_sequence("a")
      if inittone=="silence":
         self.write_sequence("")
   def lift(self,pinid):
      print("lifted ",pinid)
   def hit(self,pinid):
      t=threading.Timer(self.velocity,self.lift,[pinid])
      t.start()
      print("hit ",pinid)
   def testtone(self,tested):
      for y in range(0,6):
         if self.tones[y] == tested:
            self.hit() #lol python why are you hitting yourself
            break
   def play(self):
      for x in range(len(self.melody.notes)):
         for y in range(0,6):
            if self.tones[y] == self.melody.notes[x]:
               t=threading.Timer(self.speed*x,self.hit,[pins[y]])
               t.start()
               break
   def test(self):
      self.write_sequence("cdefgab")
      self.play()
