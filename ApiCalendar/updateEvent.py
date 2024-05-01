from conectApi import conectaApi

service =  conectaApi()

event_id = 'polqsi8r0d9dmudoip58sskofg'

updated_event = {
            'summary': 'Updated Event Summary',
            'description': 'Updated description',
            'start': {
                'dateTime': '2024-04-30T09:00:00',
                'timeZone': 'America/Sao_Paulo',
            },
            'end': {
                'dateTime': '2024-04-30T10:00:00',
                'timeZone': 'America/Sao_Paulo',
            },
        }

event = service.events().update(calendarId='primary', eventId=event_id, body=updated_event).execute()
print('Event updated: %s' % (event.get('htmlLink')))




