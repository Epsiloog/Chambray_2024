
###--------------------------------------{ INFORMATIONS }----------------------------------------------------###

"""
Bienvenu dans phoenix adventure : l'histoire intéractive
Plonge toi dans une aventure fantastique dont tu es le héro. Fait attention aux choix que tu fais.

Synopsis:
    Tu ouvres les yeux sur un tapis de mousse. Tu te relèves pour regarder où tu es. De toute évidence
tu es dans une forêt. La lumière qui filtre à travers les arbres donne un aspect surréaliste au
sous bois, comme s'il était enchanté.
Comment t’es tu retrouvé ici ? Tu n’en as pas la moindre idée. Tu ne sais ni où tu es, ni ce que
tu fais ici, ou tout ce qui précède le moment ou tu as ouvert les yeux.
Soudain tu entends, au travers des chants d’oiseaux, une voix lointaine, plusieurs voix en réalité.

Lorsqu'un choix s'offre à toi, réfléchit bien, il risque d'avoir des conséquences ....

"""

###----------------------------------------------------------------------------------------------------------###






#-----------------------{ CODE }-------------------------#
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

import graphe as g
graphe=g.Graphe()

from math import floor

## PARAMÈTRES GÉNÉRAUX ##
# couleurs
WHITE="white"
OR="#ffe169"
VERIFICATION="pink"
BLACK="black"
BLEU="#327BEC"
FIN="#2E2E2E"
THEME=WHITE

# états des boutons
ACTIF="#c49453"
DESACTIF=THEME

# polices
FontPlay = ("times", 26, "bold")
FontBouton = ("Ebrima", 10)
FontSuivant = ("Garamond", 17)
Lucida = ("Lucida Handwriting", 11)
Papyrus=("Papyrus", 11)
Segoe=("Segoe Script", 10)
Arial=("Arial", 12)
FontTexte=Lucida
#------------------------------------------------------------------------------------------------------------#

def marge(l_ecran, l_fen):
    """
    Calculer la marge à laisser entre l'écran et la fenêtre pour mettre cette dernière au centre de l'écran
    """
    return (l_ecran//2)-(l_fen//2)



#------------------------------------------------------------------------------------------------------------#

### APPLICATION PRINCIPALE  ###

class Application(tk.Tk):
    """
    Interface du jeu inclant les images, les textes et les choix d'histoires
    """
    def __init__(self):
        tk.Tk.__init__(self)

        self.graphe=g.Graphe() #lancement du graphe, pour réinitialiser à chaques parties (par défaut à 1)
        self.THEME=THEME
        self.police=True


        ## configurations de la fenêtre
        #taille de l'écran, pour s'adapter aux différents écrans de jeux
        self.w_ecran=self.winfo_screenwidth()
        self.h_ecran=self.winfo_screenheight()

        #tailles de la fenêtr selon la taille de l'écran
        self.w_fen=floor((6/7) * self.w_ecran)
        self.h_fen=floor((6/7) * self.h_ecran)

        self.title("Phœnix Adventure")
        self.geometry("%dx%d+%d+%d" %(self.w_fen, self.h_fen,
        marge(self.w_ecran,self.w_fen), marge(self.h_ecran-80,self.h_fen)))


        ## instances des tailles
        #taille des images adaptés aux dimensions de la fenêtre
        self.w_image=floor(2/3 * self.w_fen)-20
        self.h_image=floor(3/4 * self.h_fen)

        ## instances du texte
        self.texte_current=tk.StringVar(master=self) #instance qui stock le texte
        self.def_texte(self.graphe.get_text())

        ## création des Widgets
        self.creer_base()

        ## initialisation des boutons
        self.desactiver("droit")
        self.desactiver("gauche")

        ## instances des images
        #initialisation de la première image
        try:
            self.image_current = ImageTk.PhotoImage(Image.open(self.graphe.get_image()).resize((self.w_image,self.h_image),
            Image.ANTIALIAS), master=self)
        except:
            self.image_current = ImageTk.PhotoImage(Image.open("image/not_define.jpg").resize((self.w_image,self.h_image),
            Image.ANTIALIAS), master=self)

        self.image_sur_canva=self.canva_fond.create_image(0,0, anchor=tk.NW, image=self.image_current) #placement de l'image



    def validationQuitterPrinc(self):
        """
        Demande au joueur si il souhaite arrêter la partie et quitter la fenêtre principale.
        Si oui, il est redirigé vers la fenêtre d'Accueil
        """

        if not self.graphe.est_fin():
            reponse=messagebox.askokcancel("Quitter ?","Etes vous sur de vouloir quitter ? \nVous allez perdre toute votre progression !!")
        else:
            reponse=True
        if reponse:
            self.destroy()
            accueil()

    def lancer(self):
        self.bouton_suivant.config(image=self.suivant_actif)


    def rien(self):
        """
        Ne fait rien
        """
        messagebox.showinfo("Information","Malheureusement, cette fonctionnalité n'est pas disponible \ndans la version actuelle. \nAttend la prochaine mise à jour pour y avoir accès 😀.")



    def definir_image(self,n=graphe):
        """
        Changement d'image selon la place occupée dans le graphe (avancé de la partie)
        """
        try:
            self.image_current = ImageTk.PhotoImage(Image.open(n.get_image()).resize((self.w_image,self.h_image),
            Image.ANTIALIAS), master=self) #recupération et ajustement de la nouvelle image
        except:
            self.image_current = ImageTk.PhotoImage(Image.open("image/not_define.jpg").resize((self.w_image,self.h_image),
            Image.ANTIALIAS), master=self) #image de remplacement si l'image ne marche pas

        self.canva_fond.itemconfig(self.image_sur_canva, image=self.image_current) #mise en place de l'image dans le canva


    def changerTheme(self, couleur):
        self.THEME=couleur
        self.config(bg=self.THEME)
        self.label.grid_forget()
        self.bouton_gauche.grid_forget()
        self.bouton_droit.grid_forget()
        self.bouton_suivant.grid_forget()

        self.frame.config(bg=self.THEME)
        self.canva_fond.config(bg=self.THEME)
        self.canva_fond.grid(row=0, columnspan=3)
        self.labelFin=tk.Label(self.frame,
                               text=self.texte_current.get(),
                               bg=WHITE,
                               wraplength=self.w_image,
                               font=("Arial", 18)).grid(row=1, columnspan=3)
    def changerPolice(self):
        if self.police:
            self.police=False
            FontTexte=Arial
        else:
            self.police=True
            FontTexte=Papyrus
        self.label.config(font=FontTexte)


    def def_texte(self, texte_str):
        """
        configuration du texte
        """
        self.texte_current.set(texte_str)


    def get_texte(self):
        """
        obtention du texte texte_current
        """
        return self.texte_current.get()


    def activer(self, bouton):
        """
        Activer le boutons choisit et faire des configurations
        """
        b_act={"suivant":(self.bouton_suivant, self.suivant_actif), "gauche":(self.bouton_gauche, self.fleche_gauche_actif), "droit":(self.bouton_droit, self.fleche_droite_actif), "quitter":(self.bouton_quitter)}
        if bouton!="quitter":
            bout=b_act[bouton][0]
            bout['image']=b_act[bouton][1]
        else:
            bout=b_act["quitter"]
        bout['state']=tk.NORMAL


    def desactiver(self, bouton):
        """
        Desactiver le boutons choisit et faire des configurations
        """
        b_act={"suivant":self.bouton_suivant, "gauche":self.bouton_gauche, "droit":self.bouton_droit, "quitter":self.bouton_quitter}

        bout=b_act[bouton]
        if bouton!="quitter":
            bout['image']=self.bouton_desactif
        bout['state']=tk.DISABLED


    def etat_noeud(self, noeud):
        """
        Mettre les boutons dans les etats qui correspondent au noeud
        """
        if noeud.est_choix():
            self.desactiver("suivant")
            self.activer("gauche")
            self.activer("droit")

        if noeud.est_texte():
            self.activer("suivant")
            self.desactiver("gauche")
            self.desactiver("droit")
        if noeud.est_fin():
            self.desactiver("gauche")
            self.desactiver("droit")
            self.desactiver("suivant")
            self.activer("quitter")


    def aller_suivant(self):
        if self.graphe.get_noeud()==0:
            self.lancer()
        self.avancer("texte")

    def aller_gauche(self):
        self.avancer("gauche")

    def aller_droit(self):
        self.avancer("droit")


    def avancer(self, choix):
        self.graphe.avancer(choix)
        self.def_texte(self.graphe.get_text())
        self.label['text']=self.texte_current.get()

        self.definir_image(self.graphe)
        self.etat_noeud(self.graphe)

        if self.graphe.est_fin():
            self.changerTheme(FIN)



    def creer_base(self):

        ## la frame
        self.frame = tk.Frame(self,
                              bg=self.THEME,
                              width=self.w_fen, height=self.h_fen,
                              padx=10,pady=10)



        ## le texte
        self.image_texte_int=Image.open("image/parchemin.png").resize((floor(1/3 * self.w_fen),floor(4/5 * self.h_fen)), Image.ANTIALIAS)
        self.img_texte = ImageTk.PhotoImage(self.image_texte_int, master=self)

        self.label = tk.Label(self.frame,
                              text = self.texte_current.get(),
                              image = self.img_texte,
                              font=FontTexte,
                              justify=tk.LEFT,
                              bg=self.THEME,
                              compound='center',
                              width=floor(1/3 * self.w_fen)-20,height=floor(3/4 * self.h_fen),
                              wraplength=380,)



        ## les boutons
        self.bouton_desactif = ImageTk.PhotoImage(Image.open("image/desactif.png").resize((90,90), Image.ANTIALIAS), master=self.frame)

        #bouton gauche
        self.fleche_gauche_actif = ImageTk.PhotoImage(Image.open("image/gauche.png").resize((90,90), Image.ANTIALIAS), master=self.frame)
        self.bouton_gauche = tk.Button(self.frame,
                                       image=self.fleche_gauche_actif,
                                       bg=self.THEME,
                                       relief=tk.FLAT,
                                       state=tk.DISABLED,
                                       command=self.aller_gauche)

        #bouton droit
        self.fleche_droite_actif = ImageTk.PhotoImage(Image.open("image/droite.png").resize((90,90), Image.ANTIALIAS), master=self.frame)
        self.bouton_droit =  tk.Button(self.frame,
                                       image=self.fleche_droite_actif,
                                       bg=self.THEME,
                                       relief=tk.FLAT,
                                       state=tk.DISABLED,
                                       command=self.aller_droit)

        #bouton suivant
        self.suivant_actif = ImageTk.PhotoImage(Image.open("image/suivant.png").resize((250,75), Image.ANTIALIAS), master=self.frame)
        self.bout_lancer = ImageTk.PhotoImage(Image.open("image/lancer.png").resize((250,75), Image.ANTIALIAS), master=self.frame)
        self.bouton_suivant= tk.Button(self.frame,
                                       image=self.bout_lancer,
                                       bg=self.THEME,
                                       relief=tk.FLAT,
                                       command=self.aller_suivant)

        #bouton suivant
        self.bouton_quitter= tk.Button(self, text="Quitter", font=FontBouton,
                                       relief=tk.FLAT,
                                       bg='lightgrey',
                                       command=self.validationQuitterPrinc)

        ## le canva
        self.canva_fond = tk.Canvas(self.frame, bg=self.THEME,
                                    width=self.w_image, height=self.h_image)

        """
        Création d'un menu non fonctionnel pour l'instant
        """
        menu = tk.Menu(self)
        menu.add_command(label="Fonctionalités", command=self.rien)
        menu.add_command(label="Principe", command=self.rien)
        menu.add_command(label="Changer la police", command=self.changerPolice)
        # Configuration du menu dans la fenêtre
        self.config(menu = menu)



        ##les pack()
        self.frame.pack(side="top", expand=True)

        self.canva_fond.grid(row=0, column=0, columnspan=2, pady=0, ipadx=0,ipady=0)

        self.label.grid(row=0, column=2, sticky= tk.N, pady=0)

        self.bouton_quitter.place(relx=1, rely=1,anchor= tk.SE)
        self.bouton_gauche.grid(row=1, column=0, pady=20, sticky=tk.E)
        self.bouton_suivant.grid(row=1, column=1, pady=20)
        self.bouton_droit.grid(row=1, column=2, sticky=tk.W)




class Accueil(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.w_ecran=self.winfo_screenwidth()
        self.h_ecran=self.winfo_screenheight()

        self.w_fen=floor((3/4)*self.winfo_screenwidth())
        self.h_fen=floor((3/4)*self.winfo_screenheight())

        self.title("Phœnix Adventure")
        self.iconphoto(True, tk.PhotoImage(file='image\plume2.png'))
        self.configure(bg=BLACK)

        self.geometry("%dx%d+%d+%d" %(self.w_fen,self.h_fen, marge(self.w_ecran,self.w_fen), marge(self.h_ecran-50,self.h_fen)))
        self.resizable(width=False ,height=False)

        self.w_b=10
        self.h_b=1

        self.w_img=self.w_fen-2
        self.h_img=self.h_fen-2

        self.x_bouton=(self.w_fen//2)-(248//2)
        self.y_bouton=(3/4 * self.h_fen)-45



        self.creer_base()

    def validationQuitterAcc(self):
        reponse=messagebox.askokcancel("Quitter ?","Etes vous sur de vouloir quitter ?")
        if reponse:
            self.destroy()

    def rien(self):
        messagebox.showinfo("Information","Malheureusement, cette fonctionnalité n'est pas disponible \ndans la version actuelle. \nAttendez la prochaine mise à jour pour y avoir accès.")

    def lancer(self):
        jeu(self)
        #self.destroy()


    def creer_base(self):

        #image
        self.image_fond_int=Image.open("image/play.png").resize((self.w_img,self.h_img), Image.ANTIALIAS)
        self.img_fond = ImageTk.PhotoImage(self.image_fond_int, master=self)

        self.fond=tk.Label(self,image=self.img_fond, bg="black").pack()

        self.play=tk.Button(self.fond, text="Let's Play",
                            bg=BLEU,
                            fg="white",font=FontPlay,
                            width=self.w_b, height=self.h_b,
                            relief=tk.FLAT,
                            command=self.lancer).place(relx=.5, rely=.755,anchor= tk.CENTER)

        self.finDebloquee=tk.Button(self, text="Fins débloquées", justify=tk.CENTER, font=FontBouton,
                               width=15, height=1,
                               relief=tk.FLAT,
                               bg=BLACK,
                               fg=WHITE,
                               command=self.rien).place(relx=0, rely=1, anchor= tk.SW)

        self.quitter=tk.Button(self, text="Quitter", justify=tk.CENTER, font=FontBouton,
                               width=self.w_b, height=self.h_b,
                               relief=tk.FLAT,
                               bg=BLACK,
                               fg=WHITE,
                               command=self.validationQuitterAcc).place(relx=1, y=self.h_fen,anchor= tk.SE)




def jeu(acc):
        acc.destroy()
        app = Application()
        app.mainloop()

def accueil():
        acc = Accueil()
        acc.mainloop()


accueil()