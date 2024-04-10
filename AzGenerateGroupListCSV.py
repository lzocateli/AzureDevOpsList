import json
import csv


with open('merged-az-grouplist.json') as f:
    data = json.load(f)


# csv_data = [(item['displayName'], item['description']) for item in data['graphGroups']]
csv_data = [(item['displayName'], item['description']) for item in data]


with open('brazil-devops-user-groups.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['displayName', 'description'])  # escrever o cabeçalho
    writer.writerows(csv_data)  # escrever os dados

print("Os dados foram gravados com sucesso.")
