# Créé par Thomas, le 22/05/2024 en Python 3.7

from PIL import Image
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

print("Rentrez le chemin d'accès du fichier ?")
path1 = filedialog.askopenfilename()
#print(path1)
i=len(path1)-1
while(path1[i]!='/'):
    print(i)
    i-=1
f=""
for c in range(i,len(path1)-3):
    f+=path1[c]

#print(f)
image_1 = Image.open(path1)
im_1 = image_1.convert('RGB')

print("Où souhaitez-vous enregistrer le fichier pdf nouvellement créé ?")
path2 = filedialog.askdirectory()
im_1.save(path2+f+"pdf")