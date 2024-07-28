# -*- coding: utf8 -*-
from tkinter import Tk,Frame,Button,Canvas,LEFT,RIGHT,TOP,BOTTOM,BOTH,YES,E
import re

root = None
application = None
canvas = None
btnQuitter = None

def initDrawing(titre,x,y,largeur,hauteur):
   """DÃ©finition d'une fenÃªtre graphique"""
   global root,application,canvas,btnQuitter
   root = Tk()
   root.geometry("{}x{}+{}+{}".format(largeur,hauteur,x,y))
   application = Frame(root,bg="white")
   application.pack(fill=BOTH,expand=YES)
   application.master.title(titre)

   canvas = Canvas(application,bg="white",highlightthickness=0)
   canvas.pack(side=TOP,fill=BOTH,expand=YES)

#   btnQuitter = Button(application, text="Quitter", command=root.destroy)
#   btnQuitter.pack(side=RIGHT)

def drawRect(x1,y1,x2,y2,rouge,vert,bleu):
   """TracÃ© d'un rectangle"""
   global canvas
   couleur = "#%02x%02x%02x" % (rouge,vert,bleu)
   canvas.create_rectangle(x1,y1,x2,y2,outline=couleur,fill=None)

def paintRect(x1,y1,x2,y2,rouge,vert,bleu):
   """Remplissage d'un rectangle"""
   global canvas
   couleur = "#%02x%02x%02x" % (rouge,vert,bleu)
   canvas.create_rectangle(x1,y1,x2,y2,outline=couleur,fill=couleur)

def drawCircle(x,y,rayon,rouge,vert,bleu):
   """TracÃ© d'un cercle"""
   global canvas
   couleur = "#%02x%02x%02x" % (rouge,vert,bleu)
   canvas.create_oval(x-rayon,y-rayon,x+rayon,y+rayon,outline=couleur,fill=None)

def paintCircle(x,y,rayon,rouge,vert,bleu):
   """Remplissage d'un cercle (disque)"""
   global canvas
   couleur = "#%02x%02x%02x" % (rouge,vert,bleu)
   canvas.create_oval(x-rayon,y-rayon,x+rayon,y+rayon,outline=couleur,fill=couleur)

def drawPixel(x,y,rouge,vert,bleu):
   """TracÃ© d'un pixel"""
   global canvas
   couleur = "#%02x%02x%02x" % (rouge,vert,bleu)
   canvas.create_rectangle(x,y,x,y,outline=couleur)

def drawLine(x1,y1,x2,y2,rouge,vert,bleu):
   """TracÃ© d'un segment de droite"""
   global canvas
   couleur = "#%02x%02x%02x" % (rouge,vert,bleu)
   canvas.create_line(x1,y1,x2,y2,fill=couleur)

def showDrawing():
   """Affichage de la fenÃªtre graphique et attente de la fermeture"""
   global root
   root.mainloop()

word = re.compile(r"(\S)+")

class ISNfile:
   def __init__(self,nom,mode,codage):
      self.fichier = open(nom,mode,encoding=codage)
      self.tampon = ""
      self.index  = 0

   def fetch(self):
      if self.tampon == "":
         self.tampon = self.fichier.readline()
         self.index = 0
         if self.tampon == "":
            raise EOFError("fetch")
         if self.tampon[-1] == "\n":
            self.tampon = self.tampon[:-1]

   def readline(self):
      try:
         self.fetch()
         retour = self.tampon[self.index:]
         self.tampon = ""
         return retour
      except EOFError:
         raise EOFError("readline")

   def readword(self):
      try:
         while True:
            self.fetch()
            mot = word.search(self.tampon,self.index)
            if mot != None:
               self.index = mot.end()
               return mot.group(0)
            self.tampon = ""
      except EOFError:
         raise EOFError("readword")

   def write(self,message):
      self.fichier.write(message)

   def close(self):
      self.fichier.close()

class EOFError(Exception):
   def __init__(self,value):
      self.value = value
   def __repr__(self):
      return "{}: plus rien Ã  lire".format(self.value)

def ISNopen(nom,mode,codage="utf8"):
   """Ouverture du fichier Ã  la faÃ§on de open (voir doc Python)"""
   return ISNfile(nom,mode,codage)

def openIn(nom):
  f = ISNopen(nom,"r","utf-8")
  return f

def openOut(nom):
  f = ISNopen(nom,"w","utf-8")
  return f

def readLineFromFile(fichier):
   """Lecture d'une ligne depuis le fichier"""
   return fichier.readline().strip()

def readStringFromFile(fichier):
   """Lecture d'une chaÃ®ne dÃ©limitÃ© par des blancs depuis le fichier"""
   return fichier.readword()

def close(fichier):
   """Fermeture du fichier"""
   fichier.close()
