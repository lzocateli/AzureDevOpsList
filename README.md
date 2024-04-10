# AzureDevOpsUserList
- Sempre execute esse scripts dentro do container gerado com `devContainer`
- Se estiver acessando pelo primeira vez o container, execute `az login`

- O script `AzGenerateGroupList.py` cria um arquivo json com os dados dos grupos de usuarios que acessam o devops
- O script `AzGenerateGroupListCSV.py` cria um csv a partir do arquivo gerado anteriormente, somente com as colunas Nome e Descrição dos grupos.

