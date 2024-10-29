from pyexpat.errors import messages

def send_email( message, recipient, sender = 'university.help@mail.ru') :
    if '@' not in recipient or not recipient.endswith(('.com','.ru','.net')) or not sender.endswith(('.com','.ru','.net')) :
        print(f'Невозможно отправить письмо с адреса {sender} на адрес { recipient}.')
        
    elif sender == recipient :
        print('Нельзя отправить письмо самому себе.')

    elif sender == 'university.help@mail.ru' :
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')

    elif sender != 'university.help@mail.ru' :
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')

send_email('message','vasyok1337@gmail.com')

send_email('message','urban.fan@mail.ru','urban.info@gmail.com')

send_email('message','urban.student@mail.ru', 'urban.teacher@gmail.uk')

send_email('message','university.help@mail.ru', 'university.help@gmail.com')
