# CalendarAPI
Uso da API do google Calendar

aplicações que fazem um CRUD para manejo de evento via google Calendar

necessario arquivo de credenciais onde pode ser obtido no https://console.cloud.google.com/

1. conectAPI: faz a conecção com a api buscando as credenciais e gerando um token de permissao via Oauth2

2. createEvent: cria o evento via json no corpo da aplicação, gerando o id automatico pelo calendar, e a agenda principal

3. lisEvent: faz uma lista dos 10 ultimos eventos existentes

4. updateEvent: atualiza evento existente via json identificando o evento a ser alterado via ID

5. deleteEvent: deleta evento existente identificando o evento a ser deletado via ID
