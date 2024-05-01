import datetime
from conectApi import conectaApi


service = conectaApi()

        # Create an event
event = {
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

event = service.events().insert(calendarId='primary', body=event).execute()
print('Event created: %s' % (event.get('htmlLink')))



