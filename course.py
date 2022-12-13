import json
import sys
import os

action = ["1", "2", "3", "4", "5"]

Menu = """ Choisir parmis les options suivantes:
1. ajouter un produit
2. retirer un produit
3. afficher les produits
4. vider la liste de produit
5. quitter
Votre choix: """

current_dir = os.path.dirname(__file__)
path = os.path.join(current_dir,"course.json")

if not os.path.exists(path):
    liste = []
else:
    with open(path, "r", encoding="utf-8") as f:
        liste = json.load(f)

while True:
    user_choice = input(Menu)
    current_dir = os.path.dirname(__file__)
    
    if user_choice not in Menu:
        print("veuillez inséré un nombre valide!")
        continue
    if user_choice == "1":
        add = input("ajoutez votre produit: ")
        liste.append(add)
  
    elif user_choice =="2":
        delete = input("retirez votre produit: ")
        if delete in liste:
            liste.remove(delete)
            print(f"l'objet: ", delete, " a été supprimé")
        else:
            print(delete, f" n'existe pas")
    elif user_choice == "3":
        if liste:
            for i, el in enumerate(liste):
                print(i, el)
        else:
            print("la liste est vide")
    elif user_choice == "4":
        if liste: 
            liste.clear()
            print("la liste a bien été vidé")
        else:
            print("il n'y a rien a supprimé")
    elif user_choice == "5":
        with open(path, "w+", encoding="utf-8") as f:
            json.dump(liste, f, indent=4)
            print(f"Sauvegarde du fichier dans ", path,". A bientot")
        sys.exit()