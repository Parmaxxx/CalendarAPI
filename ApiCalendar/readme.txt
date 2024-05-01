como configurar a api no google cloud
https://www.youtube.com/watch?v=tvYWoHPpiMI&t=2425s
do minuto 1:58 ate 14:30
ATENÇÃO na hora de escolher o tipo da aplicação tem que ser aplicação para desktop

pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
python3 createEvent.py   Cria um evento
python3 updateEvent.py   atualiza um evento
python3 deleteEvent.py   Deleta um evento
python3 listEvent.py     Lista os 10 ultimos eventos


Estrutura do json para criar evento
{'summary': 'Updated Event Summary',
            'description': 'Updated description',
            'start': {
                'dateTime': '2024-04-30T09:00:00',
                'timeZone': 'America/Sao_Paulo',
            },
            'end': {
                'dateTime': '2024-04-30T10:00:00',
                'timeZone': 'America/Sao_Paulo',
            },}

            recurrence serve para colocar a recorrência do evento

  'recurrence': [
    'RRULE:FREQ=DAILY;COUNT=2'
  ],

  attendees serve para linkar os emails que tem relação com o evento

  'attendees': [          
    {'email': 'lpage@example.com'},
    {'email': 'sbrin@example.com'},
  ],

  reminders serve para colocar lembrete via email quando estiver acabando o evento

  'reminders': { 
    'useDefault': False,
    'overrides': [
      {'method': 'email', 'minutes': 24 * 60},
      {'method': 'popup', 'minutes': 10},
    ],
  },