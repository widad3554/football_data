import requests
import csv


url = "http://api.football-data.org/v2/competitions/2001/matches"
headers = {"X-Auth-Token": "96c8a56ee5c44d3fbf2153cd84f32558"}


response = requests.get(url, headers=headers)


data = response.json()


with open("match_data.csv", mode="w", newline="", encoding="utf-8") as csv_file:
    # Define column names for CSV file
    fieldnames = ["saison", "date_utc", "statut", "dernière_mise_à_jour",
                  "équipe_à_domicile", "équipe_à_extérieur", "vainqueur", "durée", "équipe_à_domicile_temps_complet",
                  "équipe_à_extérieur_temps_complet", "équipe_à_domicile_mi_temps", "équipe_à_extérieur_mi_temps",
                  "équipe_à_domicile_temps_supplémentaire", "équipe_à_extérieur_temps_supplémentaire", "équipe_à_domicile_penalties",
                  "équipe_à_extérieur_penalties", "arbitres_nom", "arbitres_nationalité"]


    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()


    for match in data["matches"]:
        row = {}


        row["saison"] = match["season"]["startDate"] + " - " + match["season"]["endDate"]

        # Extract date, status and update information
        #row["date_début"] = match["utcDate"][:10]
        #row["date_fin"] = match["utcDate"][:10]
        row["date_utc"] = match["utcDate"]
        row["statut"] = match["status"]
        row["dernière_mise_à_jour"] = match["lastUpdated"]


        row["équipe_à_domicile"] = match["homeTeam"]["name"]
        row["équipe_à_extérieur"] = match["awayTeam"]["name"]


        if match["score"]["winner"] is not None:
            row["vainqueur"] = match["score"]["winner"]
        else:
            row["vainqueur"] = "pas encore joué"

        row["durée"] = match["score"]["duration"]
        row["équipe_à_domicile_temps_complet"] = match["score"]["fullTime"]["homeTeam"]
        row["équipe_à_extérieur_temps_complet"] = match["score"]["fullTime"]["awayTeam"]
        row["équipe_à_domicile_mi_temps"] = match["score"]["halfTime"]["homeTeam"]
        row["équipe_à_extérieur_mi_temps"] = match["score"]["halfTime"]["awayTeam"]
        row["équipe_à_domicile_temps_supplémentaire"] = match["score"]["extraTime"]["homeTeam"]
        row["équipe_à_extérieur_temps_supplémentaire"] = match["score"]["extraTime"]["awayTeam"]
        row["équipe_à_domicile_penalties"] = match["score"]["penalties"]["homeTeam"]
        row["équipe_à_extérieur_penalties"] = match["score"]["penalties"]["awayTeam"]


        if len(match["referees"]) > 0:
            row["arbitres_nom"] = match["referees"][0]["name"]
            row["arbitres_nationalité"] = match["referees"][0]["nationality"]
        else:
            row["arbitres_nom"] = ""

.
        writer.writerow(row)

print("Les données sont enregistrées dans le fichier match_data.csv")