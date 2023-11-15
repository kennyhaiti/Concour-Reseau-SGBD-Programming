def winners():
    import os
    import csv

    laurea = {}
    csv_files = ["candidatprogrammation.csv", "candidatdatabase.csv", "candidatreseau.csv"]

    for file_name in csv_files:
        if os.path.exists(file_name):
            with open(file_name, newline="") as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    code = row["Code"]
                    laurea[code] = row

    vrai = sorted(laurea.values(), key=lambda x: float(x["Moyenne"]), reverse=True)
    top = vrai[:4]

    for student in top:
        print(student)
