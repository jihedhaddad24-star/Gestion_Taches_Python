taches = []

while True:
    print("\n=== GESTION DES TACHES ===")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Rechercher une tâche")
    print("0. Quitter")

    choix = input("Votre choix : ")

    if choix == "1":
        titre = input("Titre de la tâche : ")

        if titre.strip() == "":
            print("Erreur : le titre ne peut pas être vide.")
        else:
            taches.append(titre)
            print("Tâche ajoutée avec succès.")

    elif choix == "2":
        if len(taches) == 0:
            print("Aucune tâche disponible.")
        else:
            for i, tache in enumerate(taches, start=1):
                print(i, "-", tache)

    elif choix == "3":
        mot_cle = input("Mot-clé : ")
        trouve = False

        for i, tache in enumerate(taches, start=1):
            if mot_cle.lower() in tache.lower():
                print(i, "-", tache)
                trouve = True

        if not trouve:
            print("Aucune tâche trouvée.")

    elif choix == "0":
        print("Au revoir !")
        break

    else:
        print("Choix invalide.")

    # Fin de l'application