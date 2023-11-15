from src.model.candidat import Candidat


class CandidatReseau(Candidat):
    def __init__(self, code, nom, prenom, sexe, niveau, specialisation,
                 note, question1, question2, question3, somme, moyenne):

        super().__init__(code, nom, prenom, sexe, niveau, specialisation)
        self.__code = code
        self.__nom = nom
        self.__prenom = prenom
        self.__sexe = sexe
        self.__niveau = niveau
        self.__specialisation = specialisation
        self.note = note
        self.question1 = question1
        self.question2 = question2
        self.question3 = question3
        self.somme = somme
        self.moyenne = moyenne

    def get_candidat_reseau(self):
        return {
            "Code": self.__code,
            "Nom": self.__nom,
            "Prenom": self.__prenom,
            "Sexe": self.__sexe,
            "Niveau Universitaire": self.__niveau,
            "Specialisation": self.__specialisation,
            "Note": self.note,
            "Question 1": self.question1,
            "Question 2": self.question2,
            "Question 3": self.question3,
            "Total": self.somme,
            "Moyenne": self.moyenne
        }
