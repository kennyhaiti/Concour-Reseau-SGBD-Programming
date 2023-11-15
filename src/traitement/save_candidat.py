import csv
import os
import random
from src.model.candidat_database import CandidatDataBase
from src.model.candidat_programmation import CandidatProgrammation
from src.model.candidat_reseau import CandidatReseau


def codecandidat():
    if not os.path.exists("candidatprogrammation.csv"):
        with open("candidatprogrammation.csv", "a", newline="") as file:
            header = ["Code", "Nom", "Prenom", "Sexe", "Niveau Universitaire", "Specialisation", "Note", "Total", "Moyenne"]
            line = csv.DictWriter(file, fieldnames=header)
            line.writeheader()
            idcandidat = "CNP-" + str(int(random.uniform(0, 99099)))
            return idcandidat
    elif os.path.exists("candidatprogrammation.csv"):
        with open("candidatprogrammation.csv", "r", newline="") as file:
            line = csv.DictReader(file)
            idcandidat = "CNP-" + str(int(random.uniform(0, 99099)))
            for column in line:
                if column["Code"] != idcandidat:
                    idcandidat = idcandidat
            return idcandidat

    if not os.path.exists("candidatdatabase.csv"):
        with open("candidatdatabase.csv", "a", newline="") as file:
            header = ["Code", "Nom", "Prenom", "Sexe", "Niveau Universitaire", "Specialisation", "Note",
                      "Question 1", "Question 2",  "Total", "Moyenne"]
            line = csv.DictWriter(file, fieldnames=header)
            line.writeheader()
        idcandidat = "CNB-" + str(int(random.uniform(0, 99099)))
        return idcandidat
    elif os.path.exists("candidatdatabase.csv"):
        with open("candidatdatabase.csv", "r", newline="") as file:
            line = csv.DictReader(file)
            idcandidat = "CNB-" + str(int(random.uniform(0, 99099)))
            for column in line:
                if column["Code"] != idcandidat:
                    idcandidat = idcandidat
            return idcandidat

    if not os.path.exists("candidatreseau.csv"):
        with open("candidatreseau.csv", "a", newline="") as file:
            header = ["Code", "Nom", "Prenom", "Sexe", "Niveau Universitaire", "Specialisation", "Note", "Question 1",
                      "Question 2", "Question 3", "Total", "Moyenne"]
            line = csv.DictWriter(file, fieldnames=header)
            line.writeheader()
        idcandidat = "CNR-" + str(int(random.uniform(0, 99099)))
        return idcandidat
    elif os.path.exists("candidatreseau.csv"):
        with open("candidatreseau.csv", "r", newline="") as file:
            line = csv.DictReader(file)
            idcandidat = "CNR-" + str(int(random.uniform(0, 99099)))
            for column in line:
                if column["Code"] == idcandidat:
                    idcandidat = idcandidat
            return idcandidat


def save_programming_candidate():
    while True:
        code = codecandidat()
        nom = input("Entrer le nom : ").upper()
        if not nom.isalpha():
            print("nom invalide !")
            continue
        prenom = input("Entrer le prénom : ").capitalize()
        if not prenom.isalpha():
            print("prenom invalide !")
            continue
        while True:
            sexe = input("Entrer le sexe (m/f) : ").capitalize()
            if sexe in ["M", "F"]:
                sexe = sexe
                break
        niveau = input("Entrer le niveau universitaire : ").capitalize()
        if not (niveau.isalpha() or niveau.isdigit() or niveau.isalnum()):
            print("Niveau invalid !")
            continue
        specialisation = input("Entrer la spécialisation : ").capitalize()
        if not specialisation.isalpha():
            print("Specialisation invalide !")
            continue

        while True:
            note = float(input("Entrer la note : "))
            if 0 <= note <= 1200:
                note = note
                break
            else:
                print("La note doit etre positf et  inferieur 1200")
        somme = note
        coefficients = 1200
        moyenne = (somme / coefficients) * 100

        pro_candidate = CandidatProgrammation(code, nom, prenom, sexe, niveau, specialisation,
                                              note, somme, moyenne)
        candidat = pro_candidate.get_candidat_programation()

        with open("candidatprogrammation.csv", "a", newline="") as file:
            header = ["Code", "Nom", "Prenom", "Sexe", "Niveau Universitaire",
                      "Specialisation", "Note", "Total", "Moyenne"]
            line = csv.DictWriter(file, fieldnames=header)
            if file.tell() == 0:
                line.writeheader()
            line.writerow(candidat)
        print("Enregistrement effectuer avec succes !")
        return candidat


def save_database_candidate():
    while True:
        code = codecandidat()
        nom = input("Entrer le nom : ").upper()
        if not nom.isalpha():
            print("nom invalide !")
            continue
        prenom = input("Entrer le prénom : ").capitalize()
        if not prenom.isalpha():
            print("prenom invalide !")
            continue
        while True:
            sexe = input("Entrer le sexe (m/f) : ").capitalize()
            if sexe in ["M", "F"]:
                sexe = sexe
                break
        niveau = input("Entrer le niveau universitaire : ").capitalize()
        if not (niveau.isalpha() or niveau.isdigit() or niveau.isalnum()):
            print("Niveau invalid !")
            continue
        specialisation = input("Entrer la spécialisation : ").capitalize()
        if not specialisation.isalpha():
            print("Specialisation invalide !")
            continue
        while True:
            note = float(input("Entrer la note : "))
            if 0 <= note <= 500:
                note = note
                break
            else:
                print("La note doit etre positf et  inferieur 500")

        while True:
            question1 = float(input("Entrer la note de la question 1 : "))
            if 0 <= question1 <= 300:
                question1 = question1
                break
            else:
                print("La note doit etre positf et  inferieur 300")
        while True:
            question2 = float(input("Entrer la note de la question 2 : "))
            if 0 <= question2 <= 150:
                question2 = question2
                break
            else:
                print("La note doit etre positf et  inferieur 150")
        somme = note + question1 + question2
        coefficients = 500 + 300 + 150
        moyenne = (somme / coefficients) * 100

        datab_candidate = CandidatDataBase(code, nom, prenom, sexe, niveau, specialisation, note,
                                           question1, question2, somme, moyenne)
        candidat = datab_candidate.get_candidat_database()

        with open("candidatdatabase.csv", "a", newline="") as file:
            header = ["Code", "Nom", "Prenom", "Sexe", "Niveau Universitaire", "Specialisation", "Note",
                      "Question 1", "Question 2", "Total", "Moyenne"]
            line = csv.DictWriter(file, fieldnames=header)
            if file.tell() == 0:
                line.writeheader()
            line.writerow(candidat)
        print("Enregistrement effectuer avec succes !")
        return candidat


def save_network_candidate():
    while True:
        code = codecandidat()
        nom = input("Entrer le nom : ").upper()
        if not nom.isalpha():
            print("nom invalide !")
            continue
        prenom = input("Entrer le prénom : ").capitalize()
        if not prenom.isalpha():
            print("prenom invalide !")
            continue
        while True:
            sexe = input("Entrer le sexe (m/f) : ").capitalize()
            if sexe in ["M", "F"]:
                sexe = sexe
                break
        niveau = input("Entrer le niveau universitaire : ").capitalize()
        if not (niveau.isalpha() or niveau.isdigit() or niveau.isalnum()):
            print("Niveau invalid !")
            continue
        specialisation = input("Entrer la spécialisation : ").capitalize()
        if not specialisation.isalpha():
            print("Specialisation invalide !")
            continue
        while True:
            note = float(input("Entrer la note : "))
            if 0 <= note <= 450:
                note = note
                break
            else:
                print("La note doit etre positf et  inferieur 450")

        while True:
            question1 = float(input("Entrer la note de la question 1 : "))
            if 0 <= question1 <= 250:
                question1 = question1
                break
            else:
                print("La note doit etre positf et  inferieur 250")
        while True:
            question2 = float(input("Entrer la note de la question 2 : "))
            if 0 <= question2 <= 150:
                question2 = question2
                break
            else:
                print("La note doit etre positf et  inferieur 150")
        while True:
            question3 = float(input("Entrer la note de la question 3 : "))
            if 0 <= question3 <= 150:
                question3 = question3
                break
            else:
                print("La note doit etre positf et  inferieur 150")
        somme = note + question1 + question2
        coefficients = 450 + 250 + 150 + 150
        moyenne = (somme / coefficients) * 100

        netw_candidate = CandidatReseau(code, nom, prenom, sexe, niveau, specialisation,
                                        note, question1, question2, question3, somme, moyenne)
        candidat = netw_candidate.get_candidat_reseau()

        with open("candidatreseau.csv", "a", newline="") as file:
            header = ["Code", "Nom", "Prenom", "Sexe", "Niveau Universitaire", "Specialisation", "Note",
                      "Question 1", "Question 2", "Question 3", "Total", "Moyenne"]
            line = csv.DictWriter(file, fieldnames=header)
            if file.tell() == 0:
                line.writeheader()
            line.writerow(candidat)
        print("Enregistrement effectuer avec succes !")
        return candidat

