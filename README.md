# AzureDevOpsList
List Azure DevOps groups and users

- Exeute o comando para gerar o arquivo json com os dados de grupos de acesso
   
```bash
az devops security group list --org https://dev.azure.com/nuuvers --scope organization --subject-types aadgp > azusergroups.json
```

- Execute o programa python para gerar um csv apenas com os campos desejados, a partir do arquivo json gerado pelo az devops

```bash
./ListaUsuariosDevOps.py
```
