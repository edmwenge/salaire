num_employes = int(input("Entrez le nombre d'employés : "))

noms_employes = []
salaires_employes = []

for i in range(num_employes):
    nom = input(f"Entrez le nom de l'employé {i+1} : ")
    salaire = float(input(f"Entrez le salaire de {nom} : "))
    noms_employes.append(nom)
    salaires_employes.append(salaire)

choix = input("Voulez-vous vérifier le salaire maximum, le salaire minimum ou les deux ? (max/min/les deux) : ")

if choix == "max":
    salaire_max = max(salaires_employes)
    nom_employe_max = noms_employes[salaires_employes.index(salaire_max)]
    print(f"L'employé avec le salaire le plus élevé est {nom_employe_max} avec un salaire de {salaire_max}")
elif choix == "min":
    salaire_min = min(salaires_employes)
    nom_employe_min = noms_employes[salaires_employes.index(salaire_min)]
    print(f"L'employé avec le salaire le plus bas est {nom_employe_min} avec un salaire de {salaire_min}")
elif choix == "les deux":
    salaire_max = max(salaires_employes)
    nom_employe_max = noms_employes[salaires_employes.index(salaire_max)]
    salaire_min = min(salaires_employes)
    nom_employe_min = noms_employes[salaires_employes.index(salaire_min)]
    print(f"L'employé avec le salaire le plus élevé est {nom_employe_max} avec un salaire de {salaire_max}")
    print(f"L'employé avec le salaire le plus bas est {nom_employe_min} avec un salaire de {salaire_min}")
else:
    print(input("Choix non reconnu. Merci d'entrer 'max', 'min' ou 'les deux'."))

    if choix == "max":
        salaire_max = max(salaires_employes)
        nom_employe_max = noms_employes[salaires_employes.index(salaire_max)]
        print(f"L'employé avec le salaire le plus élevé est {nom_employe_max} avec un salaire de {salaire_max}")
    elif choix == "min":
        salaire_min = min(salaires_employes)
        nom_employe_min = noms_employes[salaires_employes.index(salaire_min)]
        print(f"L'employé avec le salaire le plus bas est {nom_employe_min} avec un salaire de {salaire_min}")
    elif choix == "les deux":
        salaire_max = max(salaires_employes)
        nom_employe_max = noms_employes[salaires_employes.index(salaire_max)]
        salaire_min = min(salaires_employes)
        nom_employe_min = noms_employes[salaires_employes.index(salaire_min)]
        print(f"L'employé avec le salaire le plus élevé est {nom_employe_max} avec un salaire de {salaire_max}")
        print(f"L'employé avec le salaire le plus bas est {nom_employe_min} avec un salaire de {salaire_min}")