# robot_voiture
Création d'un véhicule à quatre moteurs et 6 LEDs RGB commandés par un rapsberry pi, lui même piloté par un clavier ou un téléphone en bluetooth.

Ce document répertorie et apporte quelques précisions sur les fichiers de code utilisés durant notre projet. L’arborescence du dossier actuel ainsi que des images d'illustrations sont accessibles dans le dossier img.
    
    • V.1 code principal : move_keyboard.py  Ce programme fut le premier à diriger les moteurs de Flash-E en utilisant les flèches du clavier. 
    
    • V.2 finale : move_bt.py version avec commandes via l'application en bluetooth, mieux commentée.

Le fichier de configuration wpa_supplicant.conf contient les informations de connexion aux réseaux sans fil. Il a permis de se connecter au partage de connexion de mon téléphone suite à son initialisation : wpa_supplicant -c/etc/wpa_supplicant/wpa_supplicant.conf -W -iwlan0 Cela fut fondamental pour controler le raspberry pi à distance en SSH ou avec VNC Viewer.

Le script en bash lancement.sh (qui sert à lire le bruitage de moteur au démarrage sur une enceinte connectée avec un cable jack) fonctionne grâce aux modifications apportée dans le fichier asound.conf. En effet, il a été nécessaire de faire ce script car le module mixer ne détectait que les périphériques audio HDMI ou bluetooth et non un appareil connecté avec un cable jack. Néanmoins, il est plus aisé d'utiliser la solution graphique alsamixer ! lancement.sh a été rendu exécutable avec la commande : chmod 755 lancement.sh
Ensuite, il a été ajouté dans le processus crontab qui permet d'exécuter des scripts en tâche de fond à des heures ou des circonstances précises : @reboot sh /home/pi/lancement.sh > /home/pi/logs/log.txt 2>&1.  Cette ligne va permettre d'effectuer la commande sh /home/pi/lancement.sh lors du démarrage et d'enregistrer les messages d'erreur et logs dans le fichier logs/log.txt. Si nécessaire, il est donc possible de regarder les messages de "sortie" du script dans le fichier log.txt.

GPIO = General Purpose Input Output : le Raspberry Pi inclus 40 broches GPIO qui permettent de créer des circuits électroniques...

HAT = Hardware Attached on the Top : concerne la carte d'extension connectée au raspberry pi au niveau de toutes les broches GPIO. Est composé de résistances, de connectiques pour les moteurs, la caméra, les LEDs, le module ultrason/infrarouge. De nombreux fils d'alimentation sont donc reliés au HAT dont ceux apportant l'électricité venant des piles.

SSH = Secure Shell Protocol : Protocole réseau utilisé pour l’accès distant à un ordinateur. Permet l’accès au terminal d'un ordinateur depuis un autre ordinateur.

VNC = Virtual Network Computing : logiciel d’accès à distance et qui a permit de contrôler le Raspberry Pi depuis un PC avec un affichage graphique !
