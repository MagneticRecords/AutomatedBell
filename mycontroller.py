from endpoints import Controller
import os
import controller as c
import sys

class machine():
   def __init__(self):
      self.melo=c.controller()
   def changenotes(self,newnotes):
      self.melo.melody.write_sequence(newnotes)

class Default(Controller):
   def GET(self):
      os.system("sudo python ~/AutomatedBell/run.py")
      print "BOOM"
      return "BOOM"
   def POST(self,**kwargs):
      #print format(kwargs['notes'])
      #self.m=machine()
      #self.m.melo.melody.write_sequence(format(kwargs['notes']))
      #os.system("sudo python ~/AutomatedBell/run.py "+self.m.melo.melody.notes)
      if kwargs['change']!="PLAY":
         command=str(kwargs['change'])
         if command.isdigit():
            self.file=open('speeddata.txt','w')
            self.file.writelines(kwargs['change'])
            self.file.close()
         else:
            self.file=open('notedata.txt','w')
            self.file.writelines(kwargs['change'])
            self.file.close()
      else:
         self.file=open('notedata.txt','r')
         self.line=self.file.readline()
         self.file2=open('speeddata.txt','r')
         self.line2=self.file2.readline()
         os.system("sudo python ~/AutomatedBell/run.py "+self.line+" "+self.line2)
         self.file.close()
         self.file2.close()
      return 'SUCCESS' #{}'+kwargs['notes']

class Foo(Controller):
   def GET(self):
      return "BANG"
