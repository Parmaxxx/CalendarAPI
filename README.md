# CalendarAPI
Uso da API do google Calendar

aplicações que fazem um CRUD para manejo de evento via google Calendar

necessario arquivo de credenciais onde pode ser obtido no https://console.cloud.google.com/

para iniciar o projeto necessario instalar seguintes dependencias:
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

para iniciar as funçoes:
python3 createEvent.py   Cria um evento
python3 updateEvent.py   atualiza um evento
python3 deleteEvent.py   Deleta um evento
python3 listEvent.py     Lista os 10 ultimos eventos

1. conectAPI: faz a conecção com a api buscando as credenciais e gerando um token de permissao via Oauth2

2. createEvent: cria o evento via json no corpo da aplicação, gerando o id automatico pelo calendar, e a agenda principal

3. lisEvent: faz uma lista dos 10 ultimos eventos existentes

4. updateEvent: atualiza evento existente via json identificando o evento a ser alterado via ID

5. deleteEvent: deleta evento existente identificando o evento a ser deletado via ID

corpo do json 

{
          'summary': 'Test Event',
          'location': 'Somewhere',
          'description': 'A chance to test creating an event.',
          'start': {
              'dateTime': '2024-04-25T09:00:00',
              'timeZone': 'America/Sao_Paulo',
            },
            'end': {
                'dateTime': '2024-04-30T10:00:00',
                'timeZone': 'America/Sao_Paulo',
            },
        }
