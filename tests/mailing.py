from webhook_omni import main

msg_request = {
    'type':'mail',
    'message':
        '''
        Sehr geehrte Damen und Herren,
        
        hiermit möchte ich bitte einen platten Reifen melden in der Musterstraße melden.
        
        Mit freundlichen grüßen
        Mustermann
        '''
}

main(msg_request)