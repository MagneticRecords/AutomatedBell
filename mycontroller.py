#from endpoints.endpoints import Controller
from endpoints import Controller
import os
import controller as c

class Default(Controller):
   #def __init__(self):

   def GET(self):
      os.system("sudo python ~/AutomatedBell/run.py")
      x=c(.1,.1)
      x.write_sequence("cdg")
      x.play()
      print "BOOM"
      return "BOOM"
   def POST(self,**kwargs):
      print "yo"
      x.write_sequence('{}'.format(kwargs['notes']))
      x.play()
      return 'HELLO {}'.format(kwargs['notes'])

class Foo(Controller):
   def GET(self):
      return "BANG"
