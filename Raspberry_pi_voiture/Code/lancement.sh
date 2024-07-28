echo Flash-E démarre !
sudo su		#on passe en super administrateur (root)
#On récupère puis installe les packets (mplayer: lecteur audio, alsa: ensemble de programmes pour jouer des sons (incorporé dans le noyau linux), mpg123: codec permettant de lire des fichiers mp3).
#grâce à l'outils Advanced Package Tool avec comme option -Y qui répond oui aux questions posées ultérieurement.
apt-get -y install mplayer mplayer-gui alsa-base alsa-utils pulseaudio mpg123
#chargement du module snd_bcm2835
modprobe snd_bcm2835
#ajout de la ligne snd_bcm2835 à la fin des modules à charger dans le noyau au démarrage 
echo 'snd_bcm2835'  >>  /etc/modules
sudo su - pi	#retour à l'utilisateur "pi"
#amixer : interface de ligne de commande permettant de controler une carte son, au niveau de la couche ALSA.
#configuration de la sortie audio sur un le cable jack
amixer cset numid=3 1
#sélection de la carte son 1 (bcm2835 Headphones)
alsamixer -c 1
#réglage de la valeur défaut du mélangeur à 95% du son maximum
amixer sset "Master",0 95%
#lecture du mp3
mplayer /home/pi/Adeept_modifié/server/sounds/bruit-de-demarrage-voiture-2s.mp3
#suppression du packet pulseaudio et purge des fichiers crées par ce dernier
sudo apt-get -y --purge remove pulseaudio
#En effet, si cette ligne n'est pas effectuée, il y a des interférences avec l'allumage des LEDs qui utilise aussi le module snd_bcm2835