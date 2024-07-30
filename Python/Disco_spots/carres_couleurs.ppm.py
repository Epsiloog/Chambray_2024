# On créer et ouvre un fichier stocké dont l'écriture sera temporairement stocké dans la variable f
# On écris ensuite les lignes suivantes :
f=open("img\carre_rouge.ppm","w")
f.write("P3\n1000 1000\n255")
for i in range(1000000):
    f.write("\n255 0 0")
# fermeture du fichier
f.close

f=open("img\carre_green.ppm","w")
f.write("P3\n1000 1000\n255")
for i in range(1000000):
    f.write("\n0 255 0")
f.close

f=open("img\carre_blue.ppm","w")
f.write("P3\n1000 1000\n255")
for i in range(1000000):
    f.write("\n0 0 255")
f.close

"""f=open("carre_orange.ppm","w")
f.write("P3\n1000 1000\n255")
for i in range(1000000):
    f.write("\n237 127 16")
f.close"""