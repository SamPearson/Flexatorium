import random, string


def random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))


def random_email_address():
    e = random_string(10) + '@' + random_string(10) + '.' + random_string(3)
    return e


class FlexatoriumUser:
    def __init__(self,
                 email=random_email_address(),
                 username=random_string(10),
                 password=random_string(10)):
        self.email = email
        self.username = username
        self.password = password

