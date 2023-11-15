import string

from src.traitement.delete import auto_delete
from src.traitement.laureat_des_laureat import winners
from src.traitement.restore_all import restore_all_candidate
from src.traitement.restore_by_code import restore_candidate_by_code
from src.traitement.save_candidat import save_database_candidate, save_network_candidate, \
    save_programming_candidate
from src.traitement.view_candidat import view_all_candidate
from src.traitement.view_candidate_domaine import programming_domaine, database_domaine, network_domaine
from src.traitement.view_laureat import laureat_candidate

# Le menu du programme
MENULIST = [
    "Enregistrer un candidat dans son fichier respectif.",
    "Afficher tous les candidats du concours sur les 3 domaines.",
    "Afficher les informations complètes sur le lauréat des lauréats du concours.",
    "Afficher la liste des candidats suivant un domaine saisi par l’utilisateur.",
    "Afficher les informations sur les 4 premiers lauréats par ordre de moyenne.",
    "Supprimer tous les candidats dont leur moyenne est en dessous de 50.",
    "Restaurer un model supprimé par son code.",
    "Restaurer tous les candidats supprimés.",
    "Quitter le programme."
]
FORMAT = string.ascii_uppercase
DOMAINES = [
    "Programmation",
    "Base de données",
    "Réseaux"
]


def main():
    while True:
        # Le menu
        print(f"{'*' * 15} Bienvenu à l'IHSI {'*' * 15}")
        for i, (chaine, lettre) in enumerate(zip(MENULIST, FORMAT)):
            print(f"{lettre}. {chaine}")
        choix = input("👉 Entrez la lettre de votre choix: ").upper()
        print()

        match choix:
            case 'A':
                while True:
                    print(f"{'*' * 5} Dans quelle discipline incrivez-vous ? {'*' * 5}")
                    for i, chaine in enumerate(DOMAINES, 1):
                        print(f"{i}. {chaine}")
                    choix = input("👉 Entrez le numero de votre choix: ")
                    print()
                    # gestion erreur utilisation
                    if not (choix.isdigit() and int(choix) in range(1, len(DOMAINES) + 1)):
                        print('*' * 50)
                        print(f"Veillez choisir parmi les {len(DOMAINES)} options suivants.")
                        print()
                        continue
                    choix = int(choix)
                    if choix == 1:
                        save_programming_candidate()
                        break
                    elif choix == 2:
                        save_database_candidate()
                        break
                    elif choix == 3:
                        save_network_candidate()
                        break
            case 'B':
                view_all_candidate()
            case 'C':
                laureat_candidate()
            case 'D':
                while True:
                    print(f"{'*' * 5} Dans quelle discipline incrivez-vous ? {'*' * 5}")
                    for i, chaine in enumerate(DOMAINES, 1):
                        print(f"{i}. {chaine}")
                    choix = input("👉 Entrez le numero de votre choix: ")
                    print()
                    # gestion erreur utilisation
                    if not (choix.isdigit() and int(choix) in range(1, len(DOMAINES) + 1)):
                        print('*' * 50)
                        print(f"Veillez choisir parmi les {len(DOMAINES)} options suivants.")
                        print()
                        continue
                    choix = int(choix)
                    if choix == 1:
                        programming_domaine()
                        break
                    elif choix == 2:
                        database_domaine()
                        break
                    elif choix == 3:
                        network_domaine()
                        break
            case 'E':
                winners()
            case 'F':
                auto_delete()
            case 'G':
                restore_candidate_by_code()
            case 'H':
                restore_all_candidate()
            case 'I':
                print("Au revoir !!!")
                exit()
