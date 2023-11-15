import csv
import os


def auto_delete():
    liste = []
    list_candidate = []
    if os.path.exists("candidatprogrammation.csv"):
        with open("candidatprogrammation.csv", newline="") as file:
            line = csv.DictReader(file)
            for column in line:
                if float(column["Moyenne"]) < 50:
                    liste.append(column)
                if float(column["Moyenne"]) >= 50:
                    list_candidate.append(column)

        with open("candidatprogrammation.csv", "w", newline="") as file:
            header = ["Code", "Nom", "Prenom", "Sexe", "Niveau Universitaire", "Specialisation", "Note",
                      "Total", "Moyenne"]
            line = csv.DictWriter(file, fieldnames=header)
            if file.tell() == 0:
                line.writeheader()
            for column in list_candidate:
                line.writerow(column)

        with open("delete_programming_candidate.csv", "a", newline="") as file:
            header = ["Code", "Nom", "Prenom", "Sexe", "Niveau Universitaire", "Specialisation", "Note",
                      "Total", "Moyenne"]
            line = csv.DictWriter(file, fieldnames=header)
            if file.tell() == 0:
                line.writeheader()
            for column in liste:
                line.writerow(column)

    liste = []
    list_candidate = []
    if os.path.exists("candidatdatabase.csv"):
        with open("candidatdatabase.csv", newline="") as file:
            line = csv.DictReader(file)
            for column in line:
                if float(column["Moyenne"]) < 50:
                    liste.append(column)
                if float(column["Moyenne"]) >= 50:
                    list_candidate.append(column)

        with open("candidatdatabase.csv", "w", newline="") as file:
            header = ["Code", "Nom", "Prenom", "Sexe", "Niveau Universitaire", "Specialisation", "Note",
                      "Question 1", "Question 2", "Total", "Moyenne"]
            line = csv.DictWriter(file, fieldnames=header)
            if file.tell() == 0:
                line.writeheader()
            for column in list_candidate:
                line.writerow(column)

        with open("delete_db_candidate.csv", "a", newline="") as file:
            header = ["Code", "Nom", "Prenom", "Sexe", "Niveau Universitaire", "Specialisation", "Note",
                      "Question 1", "Question 2", "Total", "Moyenne"]
            line = csv.DictWriter(file, fieldnames=header)
            if file.tell() == 0:
                line.writeheader()
            for column in liste:
                line.writerow(column)
    liste = []
    list_candidate = []
    if os.path.exists("candidatreseau.csv"):
        with open("candidatreseau.csv", newline="") as file:
            line = csv.DictReader(file)
            for column in line:
                if float(column["Moyenne"]) < 50:
                    liste.append(column)
                if float(column["Moyenne"]) >= 50:
                    list_candidate.append(column)

        with open("candidatreseau.csv", "w", newline="") as file:
            header = ["Code", "Nom", "Prenom", "Sexe", "Niveau Universitaire", "Specialisation", "Note",
                      "Question 1", "Question 2", "Question 3", "Total", "Moyenne"]
            line = csv.DictWriter(file, fieldnames=header)
            if file.tell() == 0:
                line.writeheader()
            for column in list_candidate:
                line.writerow(column)

        with open("delete_network_candidate.csv", "a", newline="") as file:
            header = ["Code", "Nom", "Prenom", "Sexe", "Niveau Universitaire", "Specialisation", "Note",
                      "Question 1", "Question 2", "Question 3", "Total", "Moyenne"]
            line = csv.DictWriter(file, fieldnames=header)
            if file.tell() == 0:
                line.writeheader()
            for column in liste:
                line.writerow(column)
        print("Suppression effectuer avec succes !")