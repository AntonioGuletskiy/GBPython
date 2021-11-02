import re
#
# def email_parse(email_address):
#     result = (re.split(r'@', email_address))
#     if '.' not in result[1]:
#         print('некорректный email')
#     else:
#         new_dict = dict(username=result[0], domain=result[1])
#         print(new_dict)
#     return
#
#
# email_parse('someone@geekbrains.ru')
# email_parse('someone@geekbrainsru')

# def email_parse(email_address):
#     result = re.split(r"@", email_address)
#     if '.' not in result[1]:
#         raise ValueError(f"wrong email: {email_address}")
#     else:
#         new_dict = dict(username=result[0], domain=result[1])
#         print(new_dict)
#         return
#
#
#
# email_parse('someone@geekbrains.ru')
# email_parse('someone@geekbrainsru')
#

def email_parse(email_address):
    result = re.findall('^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$', email_address)
    if not result:
        raise ValueError(f"wrong email: {email_address}")
    else:
        result = re.split(r"@", email_address)
        new_dict = dict(username=result[0], domain=result[1])
        print(new_dict)
        return



email_parse('someone@geekbrains.ru')
email_parse('2etrov123@gmail.com')
email_parse('someone@geekbrainsru')