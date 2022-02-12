import re

def parse_email(email_adress):
    re_email = re.compile(r'(?P<user>([\w]+))@(?P<domen>[^&]+\.\w+)')
    if not re_email.match(email_adress):
        raise ValueError(f'wrong!!!: {email_adress}')
    print(re_email.match(email_adress).group())

for i in ['someone@geekbrains.ru', 'som&eone@geekbrainsru', 'someone@geekbrainsru']:
    try:
        parse_email(i)
    except ValueError as err:
        print(err)
