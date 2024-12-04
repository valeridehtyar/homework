

def send_email( message,recipient,*,sender = 'university.help@mail.ru') :
    if '@' not in recipient or not recipient.endswith(('.com','.ru','.net')) or not sender.endswith(('.com','.ru','.net')) :
        print(f'Невозможно отправить письмо с адреса {sender} на адрес { recipient}.')
        
    elif sender == recipient :
        print('Нельзя отправить письмо самому себе.')

    elif sender == 'university.help@mail.ru' :
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')

    elif sender != 'university.help@mail.ru' :
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')

send_email('message',recipient='vasyok1337@gmail.com')

send_email('message',recipient='urban.fan@mail.ru',sender= 'urban.info@gmail.com')

send_email('message',recipient='urban.student@mail.ru',sender= 'urban.teacher@gmail.uk')

send_email('message',recipient='university.help@mail.ru',sender='university.help@gmail.com')
