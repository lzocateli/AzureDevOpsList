import json
import csv

# Carregar o arquivo JSON
with open('azusergroups.json') as f:
    data = json.load(f)

# Preparar os dados para o CSV
csv_data = [(item['displayName'], item['description']) for item in data['graphGroups']]

# Escrever os dados no arquivo CSV
with open('azusergroups.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['displayName', 'description'])  # escrever o cabeçalho
    writer.writerows(csv_data)  # escrever os dados

print("Os dados foram gravados com sucesso.")
