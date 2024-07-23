# CalendarAPI

## Overview
CalendarAPI is a Python-based project leveraging the Google Calendar API to perform CRUD (Create, Read, Update, Delete) operations on calendar events. This project provides an easy interface to interact with Google Calendar using simple Python scripts.

## Features
- **Create Event**: Add new events to your Google Calendar.
- **Update Event**: Modify existing events.
- **Delete Event**: Remove events from your calendar.
- **List Events**: Retrieve the latest events from your calendar.

## Setup

### Clone the Repository:
```bash
git clone https://github.com/Parmaxxx/CalendarAPI.git
cd CalendarAPI
```

## Install Dependencies:
```bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```
Credentials:

1.Obtain your credentials file from the Google Cloud Console.

2.Place the credentials file in the project directory.

Usage
Connect to API:
```bash
python3 connectAPI.py
```
Create an Event:
```bash
python3 createEvent.py
```
Update an Event:
```bash
python3 updateEvent.py
```
Delete an Event:
```bash
python3 deleteEvent.py
```
List Events:
```bash
python3 listEvent.py
```

### JSON Structure for Events
json
```bash
{
  "summary": "Test Event",
  "location": "Somewhere",
  "description": "A chance to test creating an event.",
  "start": {
    "dateTime": "2024-04-25T09:00:00",
    "timeZone": "America/Sao_Paulo"
  },
  "end": {
    "dateTime": "2024-04-30T10:00:00",
    "timeZone": "America/Sao_Paulo"
  }
}
```

## Contributing
Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.


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
