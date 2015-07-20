class melody_class:
   def __init__(self):
      self.notes = []
   def add_note(self,addednote):
      self.notes.append(addednote)
   
class controller:
   def __init__(self,initialvelocity):
      self.velocity=initialvelocity
      self.tone=initialtone
      self.melody = melody_class()
      self.tones = []
      self.rings = []
      self.tones = ['c','d','e','f','g','a','b','C']
      self.rings = ['default','onenote','silence']
   def write_sequence(self,fullmelody):
      for x in range(len(fullmelody)):
         self.melody.add_note(fullmelody[x])
   def reset(self,inittone):
      if inittone="default":
         self.write_sequence("cdg")
      if inittone="onenote":
         self.write_sequence("a")
      if inittone="silence":
         self.write_sequence("")
         
