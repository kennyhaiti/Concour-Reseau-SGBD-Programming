import csv
import os


def laureat_candidate():
    laureat_programming = 0
    laureat_database = 0
    laureat_network = 0

    if os.path.exists("candidatprogrammation.csv"):
        with open("candidatprogrammation.csv", newline="") as file:
            line = csv.DictReader(file)
            print(f"{'*' * 5} Laureat Programmation {'*' * 5}")
            for column in line:
                laureat = float(column["Moyenne"])
                if laureat >= laureat_programming:
                    laureat_programming = laureat
                    infolaureatprogramming = column
    else:
        print("Aucun candidat enregistrer en programmation.")

    if os.path.exists("candidatdatabase.csv"):
        with open("candidatdatabase.csv", newline="") as file:
            line = csv.DictReader(file)
            print(f"{'*' * 5} Laureat base de donnees  {'*' * 5}")
            for column in line:
                laureat = float(column["Moyenne"])
                if laureat >= laureat_database:
                    laureat_database = laureat
                    infolaureatdatabase = column
    else:
        print("Aucun candidat enregistrer en base de donnees")

    if os.path.exists("candidatreseau.csv"):
        with open("candidatreseau.csv", newline="") as file:
            line = csv.DictReader(file)

            for column in line:
                laureat = float(column["Moyenne"])
                if laureat >= laureat_network:
                    laureat_network = laureat
                    infolaureatnetwork = column
    else:
        print("Aucun candidat enregistrer en reseaux.")

    max_laureat = max(
        infolaureatprogramming["Moyenne"],
        infolaureatdatabase["Moyenne"],
        infolaureatnetwork["Moyenne"]
    )
    if max_laureat == infolaureatprogramming["Moyenne"]:
        print(
            "\nCode candidat             " + infolaureatprogramming["Code"],
            "\nNom candidat              " + infolaureatprogramming["Nom"],
            "\nPrenom candidat           " + infolaureatprogramming["Prenom"],
            "\nSexe candidat             " + infolaureatprogramming["Sexe"],
            "\nNiveau universitaire      " + infolaureatprogramming["Niveau Universitaire"],
            "\nSpecialisation            " + infolaureatprogramming["Specialisation"],
            "\nNote application mobile  " + infolaureatprogramming["Note"],
            "\nTotal note candidat         " + infolaureatprogramming["Total"],
            "\nMoyenne candidat          " + infolaureatprogramming["Moyenne"],
            "\n\n-------------------------------------------------------"
        )
    if max_laureat == infolaureatdatabase["Moyenne"]:
        print(
            "\nCode candidat             " + infolaureatdatabase["Code"],
            "\nNom candidat              " + infolaureatdatabase["Nom"],
            "\nPrenom candidat           " + infolaureatdatabase["Prenom"],
            "\nSexe candidat               " + infolaureatdatabase["Sexe"],
            "\nNiveau universitaire      " + infolaureatdatabase["Niveau Universitaire"],
            "\nSpecialisation            " + infolaureatdatabase["Specialisation"],
            "\nNote application mobile  " + infolaureatdatabase["Note"],
            "\nQuestion 1                " + infolaureatdatabase["Question 1"],
            "\nQuestion 2                " + infolaureatdatabase["Question 2"],
            "\nTotal note candidat         " + infolaureatdatabase["Total"],
            "\nMoyenne candidat          " + infolaureatdatabase["Moyenne"],
            "\n\n-------------------------------------------------------")

    if max_laureat == infolaureatnetwork["Moyenne"]:

        print("\nCode candidat             " + infolaureatnetwork["Code"],
              "\nNom candidat              " + infolaureatnetwork["Nom"],
              "\nPrenom candidat           " + infolaureatnetwork["Prenom"],
              "\nSexe candidat             " + infolaureatnetwork["Sexe"],
              "\nNiveau universitaire      " + infolaureatnetwork["Niveau Universitaire"],
              "\nSpecialisation            " + infolaureatnetwork["Specialisation"],
              "\nNote application mobile  " + infolaureatnetwork["Note"],
              "\nQuestion 1                " + infolaureatnetwork["Question 1"],
              "\nQuestion 2                " + infolaureatnetwork["Question 2"],
              "\nQuestion 3                " + infolaureatnetwork["Question 3"],
              "\nTotal note candidat         " + infolaureatnetwork["Total"],
              "\nMoyenne candidat          " + infolaureatnetwork["Moyenne"],
              "\n\n-------------------------------------------------------")
