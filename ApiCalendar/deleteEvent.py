import datetime

from conectApi import conectaApi

service = conectaApi()

event_id = 'polqsi8r0d9dmudoip58sskofg'  # Replace with the ID of the event you want to delete
service.events().delete(calendarId='primary', eventId=event_id).execute()
print('Event deleted successfully.')