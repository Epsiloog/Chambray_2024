#!/usr/bin/python3
# -*- coding: utf-8 -*-

#####################################################
#													#
# Nom du programme :	BATAILLE SPATIALE			#
#													#
# Auteur :				Bruno CLÉVENOT				#
#													#
# Créé le :				03/04/2023					#
#													#
# Programmé en : 		Python 3					#
#													#
# Version :				1.0.0						#
#													#
# Licence:				GPL3						#
#													#
#####################################################

## Importation des bibliothèques
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from tkinter.simpledialog import *
import sys,os, copy, random, pickle
from datetime import date, datetime
## Fin d'importation des bibliothèques

## Fonctions et procédures
def quitter_jeu ():
	''' Quitter le jeu '''
	reponse = messagebox.askyesno("Terminer le jeu","Voulez-vous réellement quitter ? \n Cliquer « Oui » pour finir")
	if reponse :
		## On quitte le programme
		fen.quit ()

def limitNom (*args) :
	''' Procédure pour limiter nom du joueur à 15 lettres '''
	nomJoueur = varNom.get ()
	if len (nomJoueur) > 15 :
		varNom.set (nomJoueur [:15])

def cross_closing_windows():
	''' Empêche fermeture de la fenêtre via la croix de fermeture '''
	return

def handle_click (event) :
	''' Empêche le redimensionnement des colonnes du treeview principal'''
	if tree.identify_region (event.x, event.y) == "separator":
		if tree.identify_column (event.x) == '#1':
			return "break"
		if tree.identify_column (event.x) == '#2':
			return "break"
		if tree.identify_column (event.x) == '#3':
			return "break"
	if treeRecord.identify_region (event.x, event.y) == "separator":
		if treeRecord.identify_column (event.x) == '#1':
			return "break"
		if treeRecord.identify_column (event.x) == '#2':
			return "break"
		if treeRecord.identify_column (event.x) == '#3':
			return "break"
		if treeRecord.identify_column (event.x) == '#4':
			return "break"
		if treeRecord.identify_column (event.x) == '#5':
			return "break"

def ouvrir_scores () :
	''' Ouvre le fichier des records '''
	liste_x = []
	fichierPickle = open ('records\\records', 'rb')
	liste_x = pickle.load (fichierPickle)
	fichierPickle.close ()
	return liste_x

def enregister_scores () :
	''' Enregistre le fichier des records '''
	global listeRecord
	fichierPickle = open ('records\\records', 'wb')
	pickle.dump (listeRecord, fichierPickle)
	fichierPickle.close ()

def ap_jeu () :
	''' Retour à la frame de jeu '''
	frame_ap.grid_remove ()
	frame_jeu.grid ()

def jeu_ap () :
	''' Ouverture de la frame À PROPOS '''
	frame_ap.grid ()
	frame_jeu.grid_remove ()

def aide_jeu () :
	''' Retour à la frame de jeu '''
	frame_aide.grid_remove ()
	frame_jeu.grid ()

def jeu_aide () :
	''' Ouverture de la frame AIDE '''
	frame_aide.grid ()
	frame_jeu.grid_remove ()

def records_jeu () :
	''' Retour à la frame de jeu '''
	frame_records.grid_remove ()
	frame_jeu.grid ()

def jeu_records () :
	''' Ouverture de la frame RECORDS '''
	vide_treeRecord ()
	ajout_treeRecord ()
	frame_jeu.grid_remove ()
	frame_records.grid ()

def lettres () :
	''' Placement des lettres en haut du canvas de jeu '''
	for i in range (10) :
		if i == 0 :
			canvas_jeu_jeu.create_image ((i+1)*60, 0, image = imgA, anchor ="nw") 
		elif i == 1 :
			canvas_jeu_jeu.create_image ((i+1)*60, 0, image = imgB, anchor ="nw") 
		elif i == 2 :
			canvas_jeu_jeu.create_image ((i+1)*60, 0, image = imgC, anchor ="nw")
		elif i == 3 :
			canvas_jeu_jeu.create_image ((i+1)*60, 0, image = imgD, anchor ="nw")
		elif i == 4 :
			canvas_jeu_jeu.create_image ((i+1)*60, 0, image = imgE, anchor ="nw")
		elif i == 5 :
			canvas_jeu_jeu.create_image ((i+1)*60, 0, image = imgF, anchor ="nw")
		elif i == 6 :
			canvas_jeu_jeu.create_image ((i+1)*60, 0, image = imgG, anchor ="nw")
		elif i == 7 :
			canvas_jeu_jeu.create_image ((i+1)*60, 0, image = imgH, anchor ="nw")
		elif i == 8 :
			canvas_jeu_jeu.create_image ((i+1)*60, 0, image = imgI, anchor ="nw")
		elif i == 9 :
			canvas_jeu_jeu.create_image ((i+1)*60, 0, image = imgJ, anchor ="nw")

def chiffres () :
	''' Placement des chiffres ç gauche du canvas de jeu '''
	for i in range (10) :
		if i == 0 :
			canvas_jeu_jeu.create_image (0, (i+1)*60, image = img1, anchor ="nw") 
		elif i == 1 :
			canvas_jeu_jeu.create_image (0, (i+1)*60, image = img2, anchor ="nw") 
		elif i == 2 :
			canvas_jeu_jeu.create_image (0, (i+1)*60, image = img3, anchor ="nw")
		elif i == 3 :
			canvas_jeu_jeu.create_image (0, (i+1)*60, image = img4, anchor ="nw")
		elif i == 4 :
			canvas_jeu_jeu.create_image (0, (i+1)*60, image = img5, anchor ="nw")
		elif i == 5 :
			canvas_jeu_jeu.create_image (0, (i+1)*60, image = img6, anchor ="nw")
		elif i == 6 :
			canvas_jeu_jeu.create_image (0, (i+1)*60, image = img7, anchor ="nw")
		elif i == 7 :
			canvas_jeu_jeu.create_image (0, (i+1)*60, image = img8, anchor ="nw")
		elif i == 8 :
			canvas_jeu_jeu.create_image (0, (i+1)*60, image = img9, anchor ="nw")
		elif i == 9 :
			canvas_jeu_jeu.create_image (0, (i+1)*60, image = img10, anchor ="nw")

def grille () :
	''' Grille de fond sur canvas de jeu '''
	for x in range(60, 670, 60) :
		if x == 660 :
			canvas_jeu_jeu.create_line (659, 60, 659, 660, fill = 'white', width = 1)
		else :
			canvas_jeu_jeu.create_line (x, 60, x, 660, fill = 'white', width = 1)
	for y in range(60, 670, 60) :
		if y == 660 :
			canvas_jeu_jeu.create_line (60, 659, 660, 659, fill = 'white', width = 1)
		else :
			canvas_jeu_jeu.create_line (60, y, 660, y, fill = 'white', width = 1)

def grilleVisee (x,y) :
	''' Grille de visée sur canvas de jeu quand appui sur une case avec bouton gauche '''
	canvas_jeu_jeu.create_rectangle ((x+1)*60, (y+1)*60, 60*(x+2), (y+2)*60, outline = 'red', width = 3)
	if  x >= 1 :
		if y >= 1 :
			canvas_jeu_jeu.create_rectangle (x*60, y*60, 60*(x+3), (y+3)*60, outline = 'red', width = 3)
		else :
			canvas_jeu_jeu.create_rectangle (x*60, (y+1)*60, 60*(x+3), (y+3)*60, outline = 'red', width = 3)
	else :
		if y >= 1 :
			canvas_jeu_jeu.create_rectangle ((x+1)*60, y*60, 60*(x+3), (y+3)*60, outline = 'red', width = 3)
		else :
			canvas_jeu_jeu.create_rectangle ((x+1)*60, (y+1)*60, 60*(x+3), (y+3)*60, outline = 'red', width = 3)
	if (x-2)>= 0 :
		if (y-2) >= 0:
			canvas_jeu_jeu.create_rectangle ((x-1)*60, (y-1)*60, 60*(x+4), (y+4)*60, outline = 'red', width = 3)
		else :
			canvas_jeu_jeu.create_rectangle ((x-1)*60, 60, 60*(x+4), (y+4)*60, outline = 'red', width = 3)
	else :
		if (y-2) >= 0:
			canvas_jeu_jeu.create_rectangle (60, (y-1)*60, 60*(x+4), (y+4)*60, outline = 'red', width = 3)
		else :
			canvas_jeu_jeu.create_rectangle (60, 60, 60*(x+4), (y+4)*60, outline = 'red', width = 3)

def affichage (x,y) :
	''' Affichage des élémants sur canvas de jeu '''
	global tableauJeu
	canvas_jeu_jeu.delete (ALL)
	canvas_jeu_jeu.create_image (60, 60, image = imgFond, anchor = "nw")
	for ya in range (10) :
		for xa in range (10) :
			if tableauJeu [ya] [xa] == 10  :
				canvas_jeu_jeu.create_image ((xa+1)*60, (ya+1)*60, image = imgVBB, anchor = "nw")
			elif tableauJeu [ya] [xa] == 11 :
				canvas_jeu_jeu.create_image ((xa+1)*60, (ya+1)*60, image = imgVBG, anchor = "nw")
			elif tableauJeu [ya] [xa] == 12 :
				canvas_jeu_jeu.create_image ((xa+1)*60, (ya+1)*60, image = imgVBH, anchor = "nw")
			elif tableauJeu [ya] [xa] == 13 :
				canvas_jeu_jeu.create_image ((xa+1)*60, (ya+1)*60, image = imgVBD, anchor = "nw")
			elif tableauJeu [ya] [xa] == 20 :
				canvas_jeu_jeu.create_image ((xa+1)*60, (ya+1)*60, image = imgVVB, anchor = "nw")
			elif tableauJeu [ya] [xa] == 21 :
				canvas_jeu_jeu.create_image ((xa+1)*60, (ya+1)*60, image = imgVVG, anchor = "nw")
			elif tableauJeu [ya] [xa] == 22 :
				canvas_jeu_jeu.create_image ((xa+1)*60, (ya+1)*60, image = imgVVH, anchor = "nw")
			elif tableauJeu [ya] [xa] == 23 :
				canvas_jeu_jeu.create_image ((xa+1)*60, (ya+1)*60, image = imgVVD, anchor = "nw")
			elif tableauJeu [ya] [xa] == 30  :
				canvas_jeu_jeu.create_image ((xa+1)*60, (ya+1)*60, image = imgVPB, anchor = "nw")
			elif tableauJeu [ya] [xa] == 31 :
				canvas_jeu_jeu.create_image ((xa+1)*60, (ya+1)*60, image = imgVPG, anchor = "nw")
			elif tableauJeu [ya] [xa] == 32 :
				canvas_jeu_jeu.create_image ((xa+1)*60, (ya+1)*60, image = imgVPH, anchor = "nw")
			elif tableauJeu [ya] [xa] == 33 :
				canvas_jeu_jeu.create_image ((xa+1)*60, (ya+1)*60, image = imgVPD, anchor = "nw")
			elif tableauJeu [ya] [xa] == 40 :
				canvas_jeu_jeu.create_image ((xa+1)*60, (ya+1)*60, image = imgVRB, anchor = "nw")
			elif tableauJeu [ya] [xa] == 41 :
				canvas_jeu_jeu.create_image ((xa+1)*60, (ya+1)*60, image = imgVRG, anchor = "nw")
			elif tableauJeu [ya] [xa] == 42 :
				canvas_jeu_jeu.create_image ((xa+1)*60, (ya+1)*60, image = imgVRH, anchor = "nw")
			elif tableauJeu [ya] [xa] == 43 :
				canvas_jeu_jeu.create_image ((xa+1)*60, (ya+1)*60, image = imgVRD, anchor = "nw")
			elif tableauJeu [ya] [xa] == 50 :
				canvas_jeu_jeu.create_image ((xa+1)*60, (ya+1)*60, image = imgVJB, anchor = "nw")
			elif tableauJeu [ya] [xa] == 51 :
				canvas_jeu_jeu.create_image ((xa+1)*60, (ya+1)*60, image = imgVJG, anchor = "nw")
			elif tableauJeu [ya] [xa] == 52 :
				canvas_jeu_jeu.create_image ((xa+1)*60, (ya+1)*60, image = imgVJH, anchor = "nw")
			elif tableauJeu [ya] [xa] == 53 :
				canvas_jeu_jeu.create_image ((xa+1)*60, (ya+1)*60, image = imgVJD, anchor = "nw")
			elif tableauJeu [ya] [xa] == 1 or tableauJeu [ya] [xa] == 15 or tableauJeu [ya] [xa] == 25 \
				or tableauJeu [ya] [xa] == 35 or tableauJeu [ya] [xa] == 45 or tableauJeu [ya] [xa] == 55 \
				or tableauJeu [ya] [xa] == 105 or tableauJeu [ya] [xa] == 115 or tableauJeu [ya] [xa] == 125 \
				or tableauJeu [ya] [xa] == 135 or tableauJeu [ya] [xa] == 205 or tableauJeu [ya] [xa] == 215 \
				or tableauJeu [ya] [xa] == 225 or tableauJeu [ya] [xa] == 235 or tableauJeu [ya] [xa] == 305 \
				or tableauJeu [ya] [xa] == 315 or tableauJeu [ya] [xa] == 325 or tableauJeu [ya] [xa] == 335 \
				or tableauJeu [ya] [xa] == 405 or tableauJeu [ya] [xa] == 415 or tableauJeu [ya] [xa] == 425 \
				or tableauJeu [ya] [xa] ==435 or tableauJeu [ya] [xa] == 505 or tableauJeu [ya] [xa] == 515 \
				or tableauJeu [ya] [xa] == 525 or tableauJeu [ya] [xa] == 535:
				canvas_jeu_jeu.create_image ((xa+1)*60, (ya+1)*60, image = imgMarque, anchor = "nw")
	lettres () # Affichage des lettres
	chiffres () # Affichage des chiffres
	grille () # Affichage de la grille de fond
	if x != -1 and y != -1 :
		grilleVisee (x, y) # Affichage de la grille de visée si bonnes coordonnées

def binding_gauche (event) :
	''' Gestion des tirs '''
	global TX, TY, tableauJeu, partieEnCours, vaisseauxTouches, coups
	ajout = True
	if partieEnCours == True :
		posA = "" # Position dans la grille
		textT = "" # Texte à afficher dans le treeview principal
		posX = (event.x - 60) // 60 # Position du clic en X (-60 car grille commence après chiffre)
		posY = (event.y - 60) // 60 # Position du clic en Y (-60 car grille commence après lettre)
		if posX != -1 and posY != -1 : # Si position correcte
			letter = chr (65 + posX) # Lettre de la colonne
			number = posY +1 # Chiffre de la ligne
			posA = letter + str (number) # Enregistrement position
			enfants = tree.get_children('') # On récupère tous les élément du treeview principal
			nbreEnfants = len (enfants) 
			for enfant in enfants: # Pour chaque enregistrement
					valeur = tree.item(enfant, 'values') # On récupère les valeurs
					if valeur [1] == posA : # Si même position
						ajout = False # On ne permet pas l'ajout et on sort de la boucle
						break
			if ajout == True : # Si ajout permis
				if tableauJeu [posY] [posX] >= 100 : # On regarde si vaisseau invisible dans la case
					if 100 <= tableauJeu [posY] [posX] <= 135 :
						if textT == "" : # Si oui, informations vaisseau touché
							textT += "Vaisseau bleu touché"
						else :
							textT += "\nVaisseau bleu touché"
						tableauJeu [posY] [posX] = tableauJeu [posY] [posX] // 10 # On rend le vaisseau visible
						vaisseauxTouches += 1 # On calcule le nombre de vaisseaux touchés
					elif 200 <= tableauJeu [posY] [posX] <= 235 :
						if textT == "" :
							textT += "Vaisseau vert touché"
						else :
							textT += "\nVaisseau vert touché"
						tableauJeu [posY] [posX] = tableauJeu [posY] [posX] // 10
						vaisseauxTouches += 1
					elif 300 <= tableauJeu [posY] [posX] <= 335 :
						if textT == "" :
							textT += "Vaisseau violet touché"
						else :
							textT += "\nVaisseau violet touché"
						tableauJeu [posY] [posX] = tableauJeu [posY] [posX] // 10
						vaisseauxTouches += 1
					elif 400 <= tableauJeu [posY] [posX] <= 435 :
						if textT == "" :
							textT += "Vaisseau rouge touché"
						else :
							textT += "\nVaisseau rouge touché"
						tableauJeu [posY] [posX] = tableauJeu [posY] [posX] // 10
						vaisseauxTouches += 1
					elif 500 <= tableauJeu [posY] [posX] <= 535 :
						if textT == "" :
							textT += "Vaisseau jaune touché"
						else :
							textT += "\nVaisseau jaune touché"
						tableauJeu [posY] [posX] = tableauJeu [posY] [posX] // 10
						vaisseauxTouches += 1
				listeY = [] # liste des positions en Y déjà prises par clic et vérifications "vu - aperçu"
				listeX = [] # liste des positions en X déjà prises par clic et vérifications "vu - aperçu"
				for yy in range (posY-1, posY+2) : # Vérification "VU" de -1 à +1
					for xx in range (posX-1, posX+2) : # Vérification "VU" de -1 à +1
						if 0 <= yy <= 9 : # Si coordonnées correctes
							if yy not in listeY :
								listeY.append (yy)
							if 0 <= xx <= 9 : # Si coordonnées correctes
								if xx not in listeX :
									listeX.append (xx)
								if 100 <= tableauJeu [yy] [xx] <= 135 : # On vérifie si vaisseau invisible
									if textT == "" :
										textT += "Vaisseau bleu vu" # Si oui, ajout de texte d'informations
									else :
										textT += "\nVaisseau bleu vu"
								elif 200 <= tableauJeu [yy] [xx] <= 235 :
									if textT == "" :
										textT += "Vaisseau vert vu"
									else :
										textT += "\nVaisseau vert vu"
								elif 300 <= tableauJeu [yy] [xx] <= 335 :
									if textT == "" :
										textT += "Vaisseau violet vu"
									else :
										textT += "\nVaisseau violet vu"
								elif 400 <= tableauJeu [yy] [xx] <= 435 :
									if textT == "" :
										textT += "Vaisseau rouge vu"
									else :
										textT += "\nVaisseau rouge vu"
								elif 500 <= tableauJeu [yy] [xx] <= 535 :
									if textT == "" :
										textT += "Vaisseau jaune vu"
									else :
										textT += "\nVaisseau jaune vu"
				listeNo5 = [] # Liste des coordonnées à exclure de la vérification "APERCU"
				for i in listeY :
					for j in listeX :
						tup = (i,j)
						listeNo5.append (tup) # Construction de la liste avec les coordonnées des listes en X et Y
				for yy in range (posY-2, posY+3) : # Vérification "APERCU" de -2 à +2
					for xx in range (posX-2, posX+3) : # Vérification "APERCU" de -2 à +2
						if 0 <= yy <= 9 : # Si coordonnées correctes
							if 0 <= xx <= 9 : # Si coordonnées correctes
								tup2 = (yy, xx)
								if tup2 not in listeNo5 : # Si coordonnées non exclues
									if 100 <= tableauJeu [yy] [xx] <=135 : # Vérification si vaisseau invisible
										if textT == "" : # Si oui, ajout texte informations
											textT += "Vaisseau bleu aperçu"
										else :
											textT += "\nVaisseau bleu aperçu"
									elif 200 <= tableauJeu [yy] [xx] <= 235 :
										if textT == "" :
											textT += "Vaisseau vert aperçu"
										else :
											textT += "\nVaisseau vert aperçu"
									elif 300 <= tableauJeu [yy] [xx] <= 335 :
										if textT == "" :
											textT += "Vaisseau violet aperçu"
										else :
											textT += "\nVaisseau violet aperçu"
									elif 400 <= tableauJeu [yy] [xx] <= 435 :
										if textT == "" :
											textT += "Vaisseau rouge aperçu"
										else :
											textT += "\nVaisseau rouge aperçu"
									elif 500 <= tableauJeu [yy] [xx] <= 535 :
										if textT == "" :
											textT += "Vaisseau jaune aperçu"
										else :
											textT += "\nVaisseau jaune aperçu"
				if textT == "" :
					textT ="-"
				affichage (posX, posY) # On affiche le tableau
				ajout_tree (posA, textT) # On ajoute informations dans treeview principal
				coups += 1 # On met à jour nombre de coups joués
				label_coups.configure (text = "Coups joués : " + str (coups).zfill (3)) # On affiche le nombre de coups joués
				if vaisseauxTouches == 5 : # Si vaisseaux touchés égal à 5
					partieEnCours = False # On arrête la partie
					topGagnant () # On affiche informations de gagne
				elif coups >= 15 : # Sinon, si nombre de coups joués à 15
					partieEnCours = False # On arrête la partie
					showinfo ("PERDU", "PERDU !! Vous n'avez pas réussi à détruire tous les vaisseaux ennemis en 15 coups ou moins.") # Informations partie perdue
			else : # Si ajout non permis
				showinfo ("Case déjà cliquée", "Vous avez déjà cliquer sur cette case !!\nMerci d'en choisir une autre.") # Informations case déjà jouée
		TX = posX # Mise à jour coordonnées en X
		TY = posY # Mise à jour coordonnées en Y

def binding_droit (event) :
	'''' Gestion des marques '''
	global tableauJeu, TX, TY, partieEnCours
	if partieEnCours == True : # Si partie en cours
		posX = (event.x - 60) // 60 # Récupération coordonnées case cliquée en X
		posY = (event.y - 60) // 60 # Récupération coordonnées case cliquée en X
		if tableauJeu [posY] [posX] == 1 : # Si marque présente
			tableauJeu [posY] [posX] = 0 # On l'enlève
		elif tableauJeu [posY] [posX] == 0 : # Si marque absente
			tableauJeu [posY] [posX] = 1 # On la met
		elif tableauJeu [posY] [posX] % 10 == 0 : # Marque absente sur vaisseau invisible
			tableauJeu [posY] [posX] = tableauJeu [posY] [posX] + 5 # On la met
		elif tableauJeu [posY] [posX] % 10 == 5 : # Marque présente sur vaisseau invisible
			tableauJeu [posY] [posX] = tableauJeu [posY] [posX] - 5 # On la retire
		affichage (TX, TY) # on affiche le tableau

def nouvelle_partie () :
	''' Nouvelle Partie '''
	global tableauJeu, partieEnCours, tableauVide, TX, TY, coups, vaisseauxTouches, coups
	if partieEnCours == True : # Si partie en cours
		rep = askyesno ("PARTIE EN COURS", "Une partie est en cours !\n Souhaitez-vous la quitter et en recommencer une autre ?") # Demande confirmation nouvelle partie
		if not rep : # Si non
			return # Passer
		else : # Si oui
			partieEnCours = False # On met partie non en cours
			nouvelle_partie () # On relance la procédure
	else : # S pas de partie en cours
		partieEnCours = True # On met la partie en cours
		coups = 0 # On remet le nombre de coups joués à 0
		label_coups.configure (text = "Coups joués : " + str (coups)) # On affiche les coups joués
		vaisseauxTouches = 0 # On met nombre de vaisseaux touchés à 0
		vide_tree () # On vide le treeview principal d'info
		TX = -1 # On remet coordonnées non valide en X
		TY = -1 # On remet coordonnées non valide en Y
		tableauJeu [:] = [] # On vide le tableau de jeu
		tableauJeu = copy.deepcopy (tableauVide) # On le remplit de vide
		choixPositionvaisseau ("bleu")  # On place les vaisseaux
		choixPositionvaisseau ("vert")
		choixPositionvaisseau ("violet")
		choixPositionvaisseau ("rouge")
		choixPositionvaisseau ("jaune") # Fin placement vaisseaux
		affichage (TX, TY) # On affiche le tableau
		lettres () # Affichage des lettres
		chiffres () # Affichage des chiffres
		grille () # On place la grille de visualisation

def choixPositionvaisseau (couleur) :
	''' Positionnement des vaisseaux dans grille '''
	global tableauJeu
	listeDirection = ["B", "G", "H", "D"]
	direction = random.choice (listeDirection) # On choisit une direction
	if couleur == "bleu" : # Pour chaque couleur, on place un indice
		indice = 100
	elif couleur == "vert" :
		indice = 200
	elif couleur == "violet" :
		indice = 300
	elif couleur == "rouge" :
		indice = 400
	elif couleur == "jaune" :
		indice = 500
	if direction == "G": # Selon direction, on ajoute une valeur à l'indice
		indice += 10
	elif direction == "H":
		indice += 20
	elif direction == "D":
		indice += 30
	possible = False # Positionnement impossible
	while possible == False : # Tant que Positionnement impossible
		pX = random.randint (0, 9) # On calcule position en X
		pY = random.randint (0, 9) # On calcule position en Y
		if (pX == pY and pY == 2) or (pX == pY and pY == 7) or (pX == 2 and pY == 7) or (pX == 7 and pY == 2) : # Si position en C3, C8, H3,H8
			possible = False # Positionnement impossible
		elif tableauJeu [pY] [pX] != 0 : # Si case déjà remplie
			possible = False # Positionnement impossible
		else :
			possible = True # Positionnement possible
	tableauJeu [pY] [pX] = indice # On place le vaisseau

def ajout_tree (pos, texte) :
	''' Ajout de données au treeview principal '''
	nbre = len (tree.get_children()) # Calcule le nombre de données déjà dans le treeview
	listeAjout = [] # Création d'une liste
	children = tree.get_children('') # Capte toutes les données contenues dans le treeview
	for child in children: # Pour chaque donnée
		values = tree.item(child, 'values') # Récupération des données
		listeAjout.append (values) # Ajout à la liste
	nbre += 1
	tupleAjout = ("", pos, texte) # Récupération sous forme d tuple des données à ajouter
	listeAjout.append (tupleAjout) # Ajout à la liste
	vide_tree () # On vide le treeview
	color = 0 # Initialisation d'une variable couleur
	for element in listeAjout : # Pour chaque élément de la liste
		if color % 2 == 0 :
			item = tree.insert ("", END, values = element, tags = ('change',)) # Insertion données et ajout tag
			color += 1 # On change de couleur
		else :
			item = tree.insert ("", END, values = element, tags = ('nochange',)) # Insertion données et ajout tag
			color += 1 # On change de couleur
		tree.tag_configure('change', background='#b3fdff') # Configuration couleur de fond slon tag
	tree.see (item) # Montre le dernier item

def vide_tree () :
	''' Vide le treeview principal '''
	tree.delete (*tree.get_children())

def ajout_treeRecord () :
	''' Ajout de données au treeview record. Même principe qu pour treeview principal '''
	global listeRecord
	color2 = 0
	for el in listeRecord :
		if color2 % 2 == 0 :
			item = treeRecord.insert ("", END, values = el, tags = ('change',))
			color2 += 1
		else :
			item = treeRecord.insert ("", END, values = el, tags = ('nochange',))
			color2 += 1
		treeRecord.tag_configure('change', background='#b3fdff', foreground ='black')

def vide_treeRecord () :
	''' Vide le treeview record. Même principe qu pour treeview principal '''
	treeRecord.delete (*treeRecord.get_children())

def reinitialiser () :
	''' Réinitialise les records '''
	global listeRecord
	listeRecord [:] = [] # Vide la liste de records
	for i in range (10) : # Remplir 10 fois
		tupleEnristrement = ("", i+1, 100, "10/01/1971 à 00 h 00 m", "GANDALFIX") # Création tuple de base
		listeRecord. append (tupleEnristrement) # Ajout à la liste
	enregister_scores () # On enregistre la liste des records
	vide_treeRecord () # Vide le treeview Record
	ajout_treeRecord () # Rempli ce treeview

def topGagnant () :
	''' Fenêtre quand joueur a gagné '''
	global listeRecord, partieEnCours, coups, ws, hs, toplevelOK
	fengagnant = Toplevel (fen, bg = "black")
	fengagnant.resizable (height = False, width = False)
	fengagnant.title ("BATAILLE SPATIALE - GAGNE")
	frame_gagnant_titre = Frame (fengagnant, bg = "black", highlightthickness = 0, width = 1000, height = 128)
	frame_gagnant_titre.grid (row = 0, column = 0, padx = 10, pady = 10)
	frame_gagnant_titre.grid_propagate (0)
	canvas_gagnant_logo_gauche = Canvas (frame_gagnant_titre, bg = "black", bd = 0, highlightthickness = 0, width = 128, height = 128)
	canvas_gagnant_logo_gauche.grid (row = 0, column = 0, padx= 0, pady = 0)
	canvas_gagnant_logo_gauche.create_image (0, 0, image = imgLogo, anchor ='nw')
	label_gagnant_titre = ttk.Label (frame_gagnant_titre, style = "BW.TLabel", text = "BATAILLE SPATIALE", width = 20)
	label_gagnant_titre.configure (font = fonte5, background = "black")
	label_gagnant_titre.grid (row = 0, column = 1, padx = 0, pady = 0)
	canvas_gagnant_logo_droite = Canvas (frame_gagnant_titre, bg = "black", bd = 0, highlightthickness = 0, width = 128, height = 128)
	canvas_gagnant_logo_droite.grid (row = 0, column = 2, padx= 0, pady = 0)
	canvas_gagnant_logo_droite.create_image (0, 0, image = imgLogo, anchor ='nw')
	label_gagnant_info = ttk.Label (fengagnant, style = "BW.TLabel", text = "", width = 70)
	label_gagnant_info.grid (row = 1, column = 0, pady = 20)
	txtGagnant = "FÉLICITATIONS !! Vous avez détruit les cinq vaisseaux ennemis en " + str (coups) + " coups."
	pos = 0 # Position où on doit insérer record si battu
	frame_gagnant_score = Frame (fengagnant, bg = "black", highlightthickness = 0, bd = 4, relief = RIDGE)
	frame_gagnant_score.grid (row = 3, column = 0, pady = 20)
	label_score = ttk.Label (frame_gagnant_score, style = "BW.TLabel", text = "NOM : ", width = 6)
	label_score.grid (row = 0, column = 0, padx = 5, pady = 10)
	label_score.configure (anchor = E, background = "black")
	entry_fin_nom = Entry (frame_gagnant_score, relief = RIDGE, text = "", width = 20, font = fonte1, justify = LEFT, textvariable = varNom)
	entry_fin_nom.grid (row = 0, column = 1, padx = 5, pady = 10)
	btSauvegarde = ttk.Button (frame_gagnant_score, style = "BW.TButton", text = "SAUVEGARDER", width = 14, cursor = "hand2", command = lambda: sauvegarde (pos))
	btSauvegarde.grid (row = 1, column = 0, columnspan = 2, padx = 5, pady = 10)
	frame_gagnant_score.grid_remove () # On cache temporairement les scores au cas où aucun record battu
	for i in range (10) :
		if coups < listeRecord [i] [2] : # Si record battu
			toplevelOK = True # Empêche fermeture fenêtre
			for j in range (9, i, -1) : # On fait descendre les records avant la position à insérer
				po = listeRecord [j-1][1] + 1 # Récupération données de position
				listeA = list (listeRecord [j-1]) # Récupération de toutes les données
				listeA [1] = po # Changement de la donnée de position
				tup = tuple (listeA) # Transformation des données en tuple
				listeRecord [j] = tup # Modification des données dans la liste
			pos = i # Récupération position où insérer données
			txtGagnant += "\n\nVous avez également battu un record.\n\n"
			txtGagnant += "Merci de remplir le formulaire ci-joint pour enregistrer votre record." # Modification du texte d'informations
			frame_gagnant_score.grid () # On démasque la frame d'enregistrement
			entry_fin_nom.focus () # On donne le focus à la saisie du nom
			break
	label_gagnant_info.configure (text = txtGagnant, anchor = W, justify = LEFT, background = "black")
	fengagnant.grab_set() # Rend le toplevel maître
	fengagnant.focus () # Donne le focus au toplevel
	fengagnant.protocol("WM_DELETE_WINDOW",cross_closing_windows) # Empêche fermeture via croix
	fengagnant.transient (fen) # Fait toujours apparaître le toplevel devant la fenêtre principale
	fengagnant.update ()
	wgagnant = fengagnant.winfo_width ()
	hgagant = fengagnant.winfo_height ()
	agagnant = (ws - wgagnant) // 2
	bgagnant = (hs - 34 - hgagant) // 2
	fengagnant.geometry ("%dx%d+%d+%d" % (wgagnant, hgagant, agagnant, bgagnant))
	fengagnant.after (3000, verif_en_cours, fengagnant) # Vérifie, après 3 secondes, que la fenêtre peut être fermée

def verif_en_cours (fengagnant) :
	''' Vérifie que la fenêtre toplevel peut être fermée '''
	global toplevelOK, niveau, niveauMax
	if toplevelOK == True: 
		fengagnant.after (10, verif_en_cours, fengagnant) # Vérifie toutes les 10 ms si la fenêtre peut être fermée
	elif toplevelOK == False : # toplevelOK à False
		fengagnant.destroy () # Fermeture de la fenêtre

def sauvegarde (p) :
	''' Enregistrement des données quand record battu '''
	global listeRecord, coups, toplevelOK
	if varNom.get () != "" : # Si on a un nom
		listeS = list (listeRecord [p]) # Récupération des données à modifier sous forme de liste
		listeS [2] = coups # Modification dans la liste du nombre de coups
		listeS [4] = varNom.get ().upper () # Modification dans la liste du nom
		varNom.set (varNom.get ().upper ())
		today = datetime.now () # Récupération info sur date et heure du jour
		temps = str (today.hour).zfill (2) + " h " + str (today.minute).zfill (2) + " m" # Modification affichage de l'heure
		jour = str(today.day).zfill(2) + "/" + str (today.month).zfill (2) + "/" + str (today.year) # Modification affichage de la date
		dateRecord = jour + " à " + temps # Date et heure cumulées
		listeS [3] = dateRecord # Modification dans la liste de la date
		tupleS = tuple (listeS) # On transforme en tuple
		listeRecord [p] = tupleS # On intègre le tuple dans la liste des records à la position souhaitée
		enregister_scores () # On enregistre les records
		toplevelOK = False # On rend l'enregistrement comme fait pour pouvoir fermer la fenêtre toplevel
	else : # Si pas de nom
		showerror ("NOM MANQUANT", "Merci de renseigner votre nom (donnée obligatoire) !!") # Message d'info manque nom
## Fin Fonctions et procédures

## Création de la fenêtre
fen = Tk()
## Fin création de la fenêtre

## Variables et images
# Variables
fonte1 = ('Arial', 14, 'bold')
fonte2 = ('Arial', 18, 'bold')
fonte3 = ('Arial',30,'bold') 
fonte4 = ('Arial', 12, 'bold')
fonte5 = ('Arial',50,'bold')
tableauVide = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
tableauJeu = copy.deepcopy (tableauVide)
coups = 0
TX = -1
TY = -1
partieEnCours = False
vaisseauxTouches = 0
listeRecord = ouvrir_scores ()
varNom = StringVar ()
varNom.trace('w', limitNom)
toplevelOK = False
# Images
imgLogo = PhotoImage (file = 'images\\logo128.png')
imgVBB = PhotoImage (file = 'images\\xenis-blue-down-60.png')
imgVBG = PhotoImage (file = 'images\\xenis-blue-left-60.png')
imgVBH = PhotoImage (file = 'images\\xenis-blue-up-60.png')
imgVBD = PhotoImage (file = 'images\\xenis-blue-right-60.png')
imgVVB = PhotoImage (file = 'images\\xenis-green-down-60.png')
imgVVG = PhotoImage (file = 'images\\xenis-green-left-60.png')
imgVVH = PhotoImage (file = 'images\\xenis-green-up-60.png')
imgVVD = PhotoImage (file = 'images\\xenis-green-right-60.png')
imgVPB = PhotoImage (file = 'images\\xenis-purple-down-60.png')
imgVPG = PhotoImage (file = 'images\\xenis-purple-left-60.png')
imgVPH = PhotoImage (file = 'images\\xenis-purple-up-60.png')
imgVPD = PhotoImage (file = 'images\\xenis-purple-right-60.png')
imgVRB = PhotoImage (file = 'images\\xenis-red-down-60.png')
imgVRG = PhotoImage (file = 'images\\xenis-red-left-60.png')
imgVRH = PhotoImage (file = 'images\\xenis-red-up-60.png')
imgVRD = PhotoImage (file = 'images\\xenis-red-right-60.png')
imgVJB = PhotoImage (file = 'images\\xenis-yellow-down-60.png')
imgVJG = PhotoImage (file = 'images\\xenis-yellow-left-60.png')
imgVJH = PhotoImage (file = 'images\\xenis-yellow-up-60.png')
imgVJD = PhotoImage (file = 'images\\xenis-yellow-right-60.png')
imgFond = PhotoImage (file = 'images\\fond.png')
imgMarque = PhotoImage (file = 'images\\marque2.png')
imgA = PhotoImage (file = 'images\\A.png')
imgB = PhotoImage (file = 'images\\B.png')
imgC = PhotoImage (file = 'images\\C.png')
imgD = PhotoImage (file = 'images\\D.png')
imgE = PhotoImage (file = 'images\\E.png')
imgF = PhotoImage (file = 'images\\F.png')
imgG = PhotoImage (file = 'images\\G.png')
imgH = PhotoImage (file = 'images\\H.png')
imgI = PhotoImage (file = 'images\\I.png')
imgJ = PhotoImage (file = 'images\\J.png')
img1 = PhotoImage (file = 'images\\1.png')
img2 = PhotoImage (file = 'images\\2.png')
img3 = PhotoImage (file = 'images\\3.png')
img4 = PhotoImage (file = 'images\\4.png')
img5 = PhotoImage (file = 'images\\5.png')
img6 = PhotoImage (file = 'images\\6.png')
img7 = PhotoImage (file = 'images\\7.png')
img8 = PhotoImage (file = 'images\\8.png')
img9 = PhotoImage (file = 'images\\9.png')
img10 = PhotoImage (file = 'images\\10.png')
# Fin variables et images

## Styles
s = ttk.Style ()
s.theme_use ("clam")
s.map ("BW.TButton", background = [('pressed', 'blue'), ('!pressed', 'silver')], foreground = [('pressed', '#ffd700'), ('!pressed', '#007fff')])
s.configure ("BW.TButton", font = fonte1, highlightthickness = 2, anchor = CENTER, justify = CENTER)
s.configure ("BW.TLabel", font = fonte1, justify = CENTER, anchor = CENTER, border = 0, background = 'olive', foreground = '#ffd700')
s.map ("BW.Treeview", background = [('selected', '#bebebe')], foreground = [('selected', '#007fff')])
s.map ("BW.Treeview.Heading", background = [('selected', '#00c600')], foreground = [('selected', 'white')])
s.configure ("BW.Treeview.Heading", background = "#00c600",foreground = 'white', font = fonte2)
s.configure("BW.Treeview",background = '#a4fc95',foreground = '#007fff', font = fonte4,rowheight = 100)
s.map ("BW2.Treeview", background = [('selected', '#bebebe')], foreground = [('selected', '#007fff')])
s.map ("BW2.Treeview.Heading", background = [('selected', '#00c600')], foreground = [('selected', 'white')])
s.configure ("BW2.Treeview.Heading", background = "#00c600",foreground = 'white', font = fonte2)
s.configure("BW2.Treeview",background = '#a4fc95',foreground = '#007fff', font = fonte4)
## Fin styles

## Intérieur fenêtre
# 0. Généralités
fen.title ("BATAILLE SPATIALE")
fen.resizable (height=False, width=False)
fen.configure (bg = 'olive')
if sys.platform.startswith ('linux') :
	fen.iconphoto (True, PhotoImage (file = 'images\\logo.xbm'))
elif sys.platform.startswith ('win32') :
	fen.iconphoto (True, PhotoImage (file = 'images\\logo.png'))

# 1. Jeu
frame_jeu = Frame (fen, bg = "olive", highlightthickness = 0, height = 994, width = 1020)
frame_jeu.grid (row = 0, column = 0)
frame_jeu.grid_propagate (0)
frame_jeu_titre = Frame (frame_jeu, bg = "olive", highlightthickness = 0)
frame_jeu_titre.grid  (row = 0, column = 0, padx = 10, pady = 10)
canvas_jeu_titre_gauche = Canvas (frame_jeu_titre, bg = "olive", bd = 0, highlightthickness = 0, width = 128, height = 128)
canvas_jeu_titre_gauche.grid (row = 0, column = 0, padx = 0, pady = 0)
canvas_jeu_titre_gauche.create_image (0, 0, image = imgLogo, anchor = "nw")
label_jeu_titre = ttk.Label (frame_jeu_titre, style = "BW.TLabel", text = "BATAILLE SPATIALE", width = 20)
label_jeu_titre.grid (row = 0, column = 1, padx = 0, pady = 0)
label_jeu_titre.configure (font = fonte5)
canvas_jeu_titre_droite = Canvas (frame_jeu_titre, bg = "olive", bd = 0, highlightthickness = 0, width = 128, height = 128)
canvas_jeu_titre_droite.grid (row = 0, column = 2, padx = 0, pady = 0)
canvas_jeu_titre_droite.create_image (0, 0, image = imgLogo, anchor = "nw")
frame_jeu_jeu = Frame (frame_jeu, bg = "olive", highlightthickness = 0, height = 660, width = 1000)
frame_jeu_jeu.grid  (row = 1, column = 0, padx = 10, pady = 30)
frame_jeu_jeu.grid_propagate (0)
canvas_jeu_jeu = Canvas (frame_jeu_jeu, bg = "olive", bd = 0, highlightthickness = 0, width = 660, height = 660)
canvas_jeu_jeu.grid (row = 0, column = 0, rowspan = 2)
canvas_jeu_jeu.create_image (60, 60, image = imgFond, anchor = "nw")
lettres ()
chiffres ()
grille ()
frame_jeu_tree = Frame (frame_jeu_jeu, bg = "yellow", highlightthickness = 0, height = 543, width = 318)
frame_jeu_tree.grid (row = 0, column = 1, padx = 10)
frame_jeu_tree.grid_propagate (0)
tree = ttk.Treeview (frame_jeu_tree, height = 5, columns = ("ID", "CASES", "INFORMATIONS"), selectmode = "none", show = 'headings', style = 'BW.Treeview')
vsb = ttk.Scrollbar (frame_jeu_tree, orient = "vertical", command = tree.yview)
tree.configure (yscrollcommand = vsb.set)
tree.heading ('ID', text = 'ID', anchor = CENTER)
tree.heading ('CASES', text = 'Cases', anchor = CENTER)
tree.heading ('INFORMATIONS', text = 'Informations', anchor = CENTER)
tree.column ('ID', stretch = False, minwidth = 0, width = 0, anchor = CENTER)
tree.column ('CASES', stretch = False, minwidth = 90, width = 90, anchor = CENTER)
tree.column ('INFORMATIONS', stretch = False, minwidth = 210, width = 210,anchor = CENTER)
tree.grid (row = 0, column = 1, sticky = 'nsew')
vsb.grid (row = 0, column = 2, sticky = 'ns', columnspan = 2)
label_coups =ttk.Label (frame_jeu_jeu, style = "BW.TLabel", text = "Coups joués : " + str (coups).zfill (3), width = 22)
label_coups.grid (row = 1, column = 1, padx = 10, pady = 20)
label_coups.configure (font = fonte2, borderwidth = 5, relief = RIDGE)
frame_jeu_boutons = Frame (frame_jeu, bg = "olive", highlightthickness = 0, bd = 4, relief = RIDGE)
frame_jeu_boutons.grid (row = 2, column = 0, padx = 10, pady = 30)
btNP = ttk.Button (frame_jeu_boutons, style = "BW.TButton", cursor = "hand2", text = "NOUVELLE PARTIE", width = 18, command = nouvelle_partie)
btNP.grid (row = 0, column = 0, padx = 10, pady = 10)
btAide = ttk.Button (frame_jeu_boutons, style = "BW.TButton", cursor = "hand2", text = "AIDE", width = 14, command = jeu_aide)
btAide.grid (row = 0, column = 1, padx = 10, pady = 10)
btAP = ttk.Button (frame_jeu_boutons, style = "BW.TButton", cursor = "hand2", text = "À PROPOS", width = 14, command = jeu_ap)
btAP.grid (row = 0, column = 2, padx = 10, pady = 10)
btRecord = ttk.Button (frame_jeu_boutons, style = "BW.TButton", cursor = "hand2", text = "RECORDS", width = 14, command = jeu_records)
btRecord.grid (row = 0, column = 3, padx = 10, pady = 10)
btQuitter = ttk.Button (frame_jeu_boutons, style = "BW.TButton", cursor = "hand2", text = "QUITTER", width = 14, command = quitter_jeu)
btQuitter.grid (row = 0, column = 4, padx = 10, pady = 10)
nouvelle_partie ()

# 2. À Propos
frame_ap = Frame (fen, bg = "olive", highlightthickness = 0, height = 994, width = 1020)
frame_ap.grid (row = 0, column = 0)
frame_ap.grid_propagate (0)
frame_ap_titre = Frame (frame_ap, bg = "olive", highlightthickness = 0)
frame_ap_titre.grid  (row = 0, column = 0, padx = 10, pady =10)
canvas_ap_titre_gauche = Canvas (frame_ap_titre, bg = "olive", bd = 0, highlightthickness = 0, width = 128, height = 128)
canvas_ap_titre_gauche.grid (row = 0, column = 0, padx = 0, pady = 0)
canvas_ap_titre_gauche.create_image (0, 0, image = imgLogo, anchor = "nw")
label_ap_titre = ttk.Label (frame_ap_titre, style = "BW.TLabel", text = "BATAILLE SPATIALE", width = 20)
label_ap_titre.grid (row = 0, column = 1, padx = 0, pady = 0)
label_ap_titre.configure (font = fonte5)
canvas_ap_titre_droite = Canvas (frame_ap_titre, bg = "olive", bd = 0, highlightthickness = 0, width = 128, height = 128)
canvas_ap_titre_droite.grid (row = 0, column = 2, padx = 0, pady = 0)
canvas_ap_titre_droite.create_image (0, 0, image = imgLogo, anchor = "nw")
label_ap_titre_titre = ttk.Label (frame_ap, style = "BW.TLabel", text = "À PROPOS", width = 22)
label_ap_titre_titre.grid (row = 1, column = 0, pady = 87)
label_ap_titre_titre.configure (font = fonte3)
label_ap_info = ttk.Label (frame_ap, style = "BW.TLabel", text = "")
label_ap_info.grid (row = 2, column = 0, pady = 87)
txtAP = "© copyleft - Bruno CLÉVENOT - Avril 2023\n\n"
txtAP += "Jeu programmé en python 3.7 par Bruno CLÉVENOT.\n\n"
txtAP += "Graphismes par Bruno CLÉVENOT, sauf pour les vaisseaux (graphismes de Carlos\nAlface trouvés sur http://carlosalface.blogspot.pt/).\n\n"
txtAP += "Code et graphismes (sauf les vaisseaux) distribués sous licence GPL 3."
label_ap_info.configure (justify = LEFT, font = fonte2, text = txtAP, foreground = "white")
btAPRetour = ttk.Button (frame_ap, style = "BW.TButton", cursor = "hand2", text = "RETOUR AU JEU", width = 20, command = ap_jeu)
btAPRetour.grid (row = 3, column = 0, pady = 87)
frame_ap.grid_remove ()

# 3. Aide
frame_aide = Frame (fen, bg = "olive", highlightthickness = 0, width = 1020, height = 994)
frame_aide.grid (row = 0, column = 0)
frame_aide.grid_propagate (0)
frame_aide_titre = Frame (frame_aide, bg = "olive", highlightthickness = 0)
frame_aide_titre.grid  (row = 0, column = 0, padx = 10, pady =10)
canvas_aide_titre_gauche = Canvas (frame_aide_titre, bg = "olive", bd = 0, highlightthickness = 0, width = 128, height = 128)
canvas_aide_titre_gauche.grid (row = 0, column = 0, padx = 0, pady = 0)
canvas_aide_titre_gauche.create_image (0, 0, image = imgLogo, anchor = "nw")
label_aide_titre = ttk.Label (frame_aide_titre, style = "BW.TLabel", text = "BATAILLE SPATIALE", width = 20)
label_aide_titre.grid (row = 0, column = 1, padx = 0, pady = 0)
label_aide_titre.configure (font = fonte5)
canvas_aide_titre_droite = Canvas (frame_aide_titre, bg = "olive", bd = 0, highlightthickness = 0, width = 128, height = 128)
canvas_aide_titre_droite.grid (row = 0, column = 2, padx = 0, pady = 0)
canvas_aide_titre_droite.create_image (0, 0, image = imgLogo, anchor = "nw")
label_aide_titre_titre = ttk.Label (frame_aide, style = "BW.TLabel", text = "AIDE", width = 22)
label_aide_titre_titre.grid (row = 1, column = 0, pady = 70)
label_aide_titre_titre.configure (font = fonte3)
label_aide_info = ttk.Label (frame_aide, style = "BW.TLabel", text = "")
label_aide_info.grid (row = 2, column = 0, pady = 71)
txtAide = "BUT :\n"
txtAide += "Trouver les cinq vaisseaux ennemis (de couleurs différentes) en 15 coups maximum.\n\n"
txtAide += "CONTRAINTES :\n"
txtAide += "Cliquer sur une case du plateau :\n"
txtAide += "• Avec le bouton gauche de la souris pour provoquer un tir. \n"
txtAide += "  Une grille rouge apparaît alors autour de la case cliquée. \n"
txtAide += "  Des informations apparaissent également sur le tableau de droite :\n"
txtAide += "  1. Un vaisseau 'détruit' est sur la case cliquée (il est alors dévoilé sur le plateau de jeu).\n"
txtAide += "  2. Un vaisseau 'vu' est situé dans l'une des 8 cases adjacentes (carré rouge de 3 x 3 cases).\n"
txtAide += "  3. Un vaisseau 'aperçu' est situé dans l'une des 16 cases adjacentes (carré rouge de 5 x 5 cases).\n"
txtAide += "• Avec le bouton droit de la souris pour gérer le placement de marques (indiquant les cases où le joueur\n  pense qu'aucun vaisseau n'est présent)."
txtAide += " L'appui sur une case vide fait apparaître une marque. Un clic sur\n  une case où une marque est présente la fait disparaître.\n"
label_aide_info.configure (justify = LEFT, text = txtAide, foreground = "white")
btAideRetour = ttk.Button (frame_aide, style = "BW.TButton", cursor = "hand2", text = "RETOUR AU JEU", width = 20, command = aide_jeu)
btAideRetour.grid (row = 3, column = 0, pady = 65)
frame_aide.grid_remove ()

# 4. Records
frame_records = Frame (fen, bg = "olive", highlightthickness = 0, width = 1020, height = 994)
frame_records.grid (row = 0, column = 0)
frame_records.grid_propagate (0)
frame_records_titre = Frame (frame_records, bg = "olive", highlightthickness = 0)
frame_records_titre.grid  (row = 0, column = 0, padx = 10, pady =10)
canvas_records_titre_gauche = Canvas (frame_records_titre, bg = "olive", bd = 0, highlightthickness = 0, width = 128, height = 128)
canvas_records_titre_gauche.grid (row = 0, column = 0, padx = 0, pady = 0)
canvas_records_titre_gauche.create_image (0, 0, image = imgLogo, anchor = "nw")
label_records_titre = ttk.Label (frame_records_titre, style = "BW.TLabel", text = "BATAILLE SPATIALE", width = 20)
label_records_titre.grid (row = 0, column = 1, padx = 0, pady = 0)
label_records_titre.configure (font = fonte5)
canvas_records_titre_droite = Canvas (frame_records_titre, bg = "olive", bd = 0, highlightthickness = 0, width = 128, height = 128)
canvas_records_titre_droite.grid (row = 0, column = 2, padx = 0, pady = 0)
canvas_records_titre_droite.create_image (0, 0, image = imgLogo, anchor = "nw")
label_records_titre_titre = ttk.Label (frame_records, style = "BW.TLabel", text = "RECORDS", width = 22)
label_records_titre_titre.grid (row = 1, column = 0, pady = 124)
label_records_titre_titre.configure (font = fonte3)
frame_records_tree = Frame (frame_records, bg = "olive", highlightthickness = 0, height = 243, width = 804)
frame_records_tree.grid (row = 2, column = 0, padx = 10)
frame_records_tree.grid_propagate (0)
treeRecord = ttk.Treeview (frame_records_tree, height = 10, columns = ("ID", "POSITION", "RECORD", "DATE", "NOM"), selectmode = "none", show = 'headings', style ="BW2.Treeview")
treeRecord.heading ('ID', text = 'ID', anchor = CENTER)
treeRecord.heading ('POSITION', text = 'Position', anchor = CENTER)
treeRecord.heading ('RECORD', text = 'Record', anchor = CENTER)
treeRecord.heading ('DATE', text = 'Date', anchor = CENTER)
treeRecord.heading ('NOM', text = 'Nom', anchor = CENTER)
treeRecord.column ('ID', stretch = False, minwidth = 0, width = 0, anchor = CENTER)
treeRecord.column ('POSITION', stretch = False, minwidth = 140, width = 140, anchor = CENTER)
treeRecord.column ('RECORD', stretch = False, minwidth = 120, width = 120,anchor = CENTER)
treeRecord.column ('DATE', stretch = False, minwidth = 320, width = 320,anchor = CENTER)
treeRecord.column ('NOM', stretch = False, minwidth = 220, width = 220,anchor = CENTER)
treeRecord.grid (row = 0, column = 0,sticky = 'nsew')
ajout_treeRecord ()
frame_records_boutons = Frame (frame_records, bg = "olive", highlightthickness = 0)
frame_records_boutons.grid (row = 3, column = 0, pady = 123)
btRecordsRetour = ttk.Button (frame_records_boutons, style = "BW.TButton", cursor = "hand2", text = "RETOUR AU JEU", width = 20, command = records_jeu)
btRecordsRetour.grid (row = 0, column = 0, padx = 100, pady = 10)
btReinitialiser = ttk.Button (frame_records_boutons, style = "BW.TButton", cursor = "hand2", text = "RÉINITIALISER", width = 20, command = reinitialiser)
btReinitialiser.grid (row = 0, column = 1, padx = 100 ,pady = 10)
frame_records.grid_remove ()
## Fin intérieur fenêtre

## Placement de la fenêtre
fen.update ()
w = fen.winfo_width ()
h = fen.winfo_height ()
ws = fen.winfo_screenwidth ()
hs = fen.winfo_screenheight ()
a = (ws - w) // 2
b = (hs - h -34) // 2
fen.geometry ("%dx%d+%d+%d" % (w, h, a, b))
## Fin placement de la fenêtre

## Fonction de fermeture de la fenêtre
fen.protocol ("WM_DELETE_WINDOW", quitter_jeu)
## Fin fonction fermeture de fenêtre

## Fonction binding
canvas_jeu_jeu.bind ('<Button-1>', binding_gauche)
canvas_jeu_jeu.bind ('<Button-3>', binding_droit)
tree.bind ('<Button-1>', handle_click)
treeRecord.bind ('<Button-1>', handle_click)
# Fin fonction binding

fen.mainloop ()