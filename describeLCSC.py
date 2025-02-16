import requests
import csv
import os

def get_lcsc_descriptions(part_numbers):
    base_url = "https://cart.jlcpcb.com/shoppingCart/smtGood/getComponentDetail"
    descriptions = {}

    for part_number in part_numbers:
        try:
            response = requests.get(f"{base_url}?componentCode={part_number}", timeout=10)
            response.raise_for_status()
            data = response.json()
            if data.get('code') == 200 and 'data' in data:
                component_data = data['data']
                descriptions[part_number] = {
                    'datasheet': component_data.get('dataManualUrl', "Lien non trouvé."),
                    'description': component_data.get('describe', "Description non trouvée.")
                }
            else:
                descriptions[part_number] = {
                    'datasheet': "Composant non trouvé ou erreur dans l'API.",
                    'description': "Composant non trouvé ou erreur dans l'API."
                }
        except Exception as e:
            descriptions[part_number] = {
                'datasheet': f"Erreur: {str(e)}",
                'description': f"Erreur: {str(e)}"
            }

    return descriptions

def update_csv_with_descriptions(input_file, output_file, descriptions):
    try:
        with open(input_file, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            fieldnames = reader.fieldnames
            if 'Datasheet' not in fieldnames:
                fieldnames.append('Datasheet')
            if 'Description' not in fieldnames:
                fieldnames.append('Description')
            rows = []
            for row in reader:
                lcsc_code = row.get('LCSC', row.get('LCSC Part', ''))
                if lcsc_code in descriptions:
                    row['Datasheet'] = descriptions[lcsc_code]['datasheet']
                    row['Description'] = descriptions[lcsc_code]['description']
                rows.append(row)
        with open(output_file, mode='w', encoding='utf-8', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
    except Exception as e:
        print(f"Erreur lors de la mise à jour du fichier CSV: {str(e)}")

if __name__ == "__main__":
    input_csv = input("Entrez le chemin du fichier CSV à modifier: ").strip()
    if not os.path.isfile(input_csv):
        print("Erreur: Le fichier spécifié n'existe pas.")
        exit(1)
    output_csv = os.path.join(os.path.dirname(input_csv), "output.csv")
    
    try:
        with open(input_csv, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            part_numbers = [row.get('LCSC', row.get('LCSC Part', '')) for row in reader if 'LCSC' in row or 'LCSC Part' in row]
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier CSV: {str(e)}")
        part_numbers = []
    
    results = get_lcsc_descriptions(part_numbers)
    update_csv_with_descriptions(input_csv, output_csv, results)
    print(f"Datasheet et descriptions mises à jour dans {output_csv}")
