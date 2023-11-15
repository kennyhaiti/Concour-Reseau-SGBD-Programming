import csv
import os


def view_all_candidate():
    if os.path.exists("candidatprogrammation.csv"):
        with open("candidatprogrammation.csv", newline="") as file:
            line = csv.DictReader(file)
            print(f"{'*' * 15} Voici la liste de tout les candidats {'*' * 15}\n")
            print(f"{'*' * 15} Candidats Programmation  {'*' * 15}\n")
            for column in line:
                print(
                    "\nCode candidat             " + column["Code"],
                    "\nNom candidat              " + column["Nom"],
                    "\nPrenom candidat           " + column["Prenom"],
                    "\nSexe candidat             " + column["Sexe"],
                    "\nNiveau universitaire      " + column["Niveau Universitaire"],
                    "\nSpecialisation            " + column["Specialisation"],
                    "\nNote application mobile  " + column["Note"],
                    "\nTotal note candidat         " + column["Total"],
                    "\nMoyenne candidat          " + column["Moyenne"],
                    "\n\n-------------------------------------------------------"
                )
    else:
        print(" Liste programmation vide")

    if os.path.exists("candidatdatabase.csv"):
        with open("candidatdatabase.csv", newline="") as file:
            line = csv.DictReader(file)
            print(f"{'*' * 15} Candidats base de donnees {'*' * 15}\n")
            for column in line:
                print(
                    "\nCode candidat             " + column["Code"],
                    "\nNom candidat              " + column["Nom"],
                    "\nPrenom candidat           " + column["Prenom"],
                    "\nSexe candidat             " + column["Sexe"],
                    "\nNiveau universitaire      " + column["Niveau Universitaire"],
                    "\nSpecialisation            " + column["Specialisation"],
                    "\nNote application mobile  " + column["Note"],
                    "\nQuestion 1                " + column["Question 1"],
                    "\nQuestion 2                " + column["Question 2"],
                    "\nTotal note candidat         " + column["Total"],
                    "\nMoyenne candidat          " + column["Moyenne"],
                    "\n\n-------------------------------------------------------"
                )
    else:
        print(" Liste base de donnees vide")

    if os.path.exists("candidatreseau.csv"):
        with open("candidatreseau.csv", newline="") as file:
            line = csv.DictReader(file)
            print(f"{'*' * 15} Candidats Reseaux {'*' * 15}\n")
            for column in line:
                print(
                    "\nCode candidat             " + column["Code"],
                    "\nNom candidat              " + column["Nom"],
                    "\nPrenom candidat           " + column["Prenom"],
                    "\nSexe candidat             " + column["Sexe"],
                    "\nNiveau universitaire      " + column["Niveau Universitaire"],
                    "\nSpecialisation            " + column["Specialisation"],
                    "\nNote application mobile  " + column["Note"],
                    "\nQuestion 1                " + column["Question 1"],
                    "\nQuestion 2                " + column["Question 2"],
                    "\nQuestion 3                " + column["Question 3"],
                    "\nTotal note candidat         " + column["Total"],
                    "\nMoyenne candidat          " + column["Moyenne"],
                    "\n\n-------------------------------------------------------"
                )
    else:
        print(" Liste reseaux vide")
