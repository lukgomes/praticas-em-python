import re

right_mail = 'user@mails.com'
wrong_mail = 'anythingmail.com'
another_wrong_mail = "another@anyother"
email = "lucas.francisco@ahsr.org.br"

MASK_MAIL = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

def mail_analisys(mail):
    if re.match(MASK_MAIL, mail):
        return ('Email is valid')
    else:
        return ('Email isn\'t valid')


print(mail_analisys(right_mail))
print(mail_analisys(wrong_mail))
print(mail_analisys(another_wrong_mail))
print(mail_analisys(email))
