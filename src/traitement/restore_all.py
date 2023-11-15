import csv
import os


def restore_all_candidate():
    liste = []
    if os.path.exists("delete_programming_candidate.csv"):
        with open("delete_programming_candidate.csv", newline="") as file:
            line = csv.DictReader(file)
            for column in line:
                liste.append(column)
        with open("delete_programming_candidate.csv", "w", newline="") as file:
            header = ["Code", "Nom", "Prenom", "Sexe", "Niveau Universitaire", "Specialisation", "Note",
                      "Total", "Moyenne"]
            line = csv.DictWriter(file, fieldnames=header)
            if file.tell() == 0:
                line.writeheader()
            for colum in liste:
                try:
                    line.writerow("")
                except AttributeError:
                    pass

        with open("candidatprogrammation.csv", "a", newline="") as file:
            header = ["Code", "Nom", "Prenom", "Sexe", "Niveau Universitaire", "Specialisation", "Note",
                      "Total", "Moyenne"]
            line = csv.DictWriter(file, fieldnames=header)
            if file.tell() == 0:
                line.writeheader()
            for colum in liste:
                line.writerow(colum)

    if os.path.exists("delete_db_candidate.csv"):
        with open("delete_db_candidate.csv", newline="") as file:
            line = csv.DictReader(file)
            for column in line:
                liste.append(column)
        with open("delete_db_candidate.csv", "w", newline="") as file:
            header = ["Code", "Nom", "Prenom", "Sexe", "Niveau Universitaire", "Specialisation", "Note",
                      "Question 1", "Question 2", "Total", "Moyenne"]
            line = csv.DictWriter(file, fieldnames=header)
            if file.tell() == 0:
                line.writeheader()
            for colum in liste:
                try:
                    line.writerow("")
                except AttributeError:
                    pass

        with open("candidatdatabase.csv", "a", newline="") as file:
            header = ["Code", "Nom", "Prenom", "Sexe", "Niveau Universitaire", "Specialisation", "Note",
                      "Question 1", "Question 2", "Total", "Moyenne"]
            line = csv.DictWriter(file, fieldnames=header)
            if file.tell() == 0:
                line.writeheader()
            for colum in liste:
                line.writerow(colum)

    if os.path.exists("delete_network_candidate.csv"):
        with open("delete_network_candidate.csv", newline="") as file:
            line = csv.DictReader(file)
            for column in line:
                liste.append(column)
        with open("delete_network_candidate.csv", "w", newline="") as file:
            header = ["Code", "Nom", "Prenom", "Sexe", "Niveau Universitaire", "Specialisation", "Note",
                      "Question 1", "Question 2", "Question 3", "Total", "Moyenne"]
            line = csv.DictWriter(file, fieldnames=header)
            if file.tell() == 0:
                line.writeheader()
            for colum in liste:
                try:
                    line.writerow("")
                except AttributeError:
                    pass

        with open("candidatreseau.csv", "a", newline="") as file:
            header = ["Code", "Nom", "Prenom", "Sexe", "Niveau Universitaire", "Specialisation", "Note",
                      "Question 1", "Question 2", "Question 3", "Total", "Moyenne"]
            line = csv.DictWriter(file, fieldnames=header)
            if file.tell() == 0:
                line.writeheader()
            for colum in liste:
                line.writerow(colum)
        print("Restoration effectuer avec succes !")
