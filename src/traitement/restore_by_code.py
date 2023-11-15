import csv
import os


def restore_candidate_by_code():
    liste = []
    list_candidate = []
    code_to_restore = input("Entre le code du candidat a restaurer: -")
    seach = code_to_restore[0:3]
    code_dispo = ["CNP", "CNB", "CNR"]
    if seach == code_dispo[0:3]:
        if os.path.exists("delete_programming_candidate.csv"):
            with open("delete_programming_candidate.csv", newline="") as file:
                line = csv.DictReader(file)
                for column in line:
                    if column["Code"] == code_to_restore:  # < ,50
                        liste.append(column)
                        print(column)
                    else:
                        list_candidate.append(column)  # >50
                        print(list_candidate)

                with open("candidatprogrammation.csv", "w", newline="") as file:
                    header = ["Code", "Nom", "Prenom", "Sexe", "Niveau Universitaire", "Specialisation", "Note",
                              "Total", "Moyenne"]
                    line = csv.DictWriter(file, fieldnames=header)
                    if file.tell() == 0:
                        line.writeheader()
                    for colum in list_candidate:
                        line.writerow(colum)

        if os.path.exists("delete_db_candidate.csv"):
            with open("delete_db_candidate.csv", newline="") as file:
                line = csv.DictReader(file)
                for column in line:
                    if column["Code"] == code_to_restore:  # < ,50
                        liste.append(column)
                        print(column)
                    else:
                        list_candidate.append(column)  # >50
                        print(list_candidate)

                with open("candidatdatabase.csv", "w", newline="") as file:
                    header = ["Code", "Nom", "Prenom", "Sexe", "Niveau Universitaire", "Specialisation", "Note",
                              "Question 1", "Question 2", "Total", "Moyenne"]
                    line = csv.DictWriter(file, fieldnames=header)
                    if file.tell() == 0:
                        line.writeheader()
                    for colum in list_candidate:
                        line.writerow(colum)

        if os.path.exists("delete_network_candidate.csv"):
            with open("delete_network_candidate.csv", newline="") as file:
                line = csv.DictReader(file)
                for column in line:
                    if column["Code"] == code_to_restore:  # < ,50
                        liste.append(column)
                        print(column)
                    else:
                        list_candidate.append(column)  # >50
                        print(list_candidate)

                with open("candidatreseau.csv", "w", newline="") as file:
                    header = ["Code", "Nom", "Prenom", "Sexe", "Niveau Universitaire", "Specialisation", "Note",
                              "Question 1", "Question 2", "Question 3", "Total", "Moyenne"]
                    line = csv.DictWriter(file, fieldnames=header)
                    if file.tell() == 0:
                        line.writeheader()
                    for colum in list_candidate:
                        line.writerow(colum)
                print("Le fichier a ete restaurer avec succes !")



