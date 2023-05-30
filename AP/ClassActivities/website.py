import re


class Account:
    def __init__(self, username, password, email):
        self.username = username
        self.email = email
        self.password = password

    @staticmethod
    def check_username(username):
        return re.match(r"^[A-z]+_[A-z]+$", username) is not None

    @staticmethod
    def check_password(password):
        return re.match(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)\w{8,}", password) is not None

    @staticmethod
    def check_email(email):
        return re.match(r"^[\w.]+@(\w+\.)+\w{2,5}$", email) is not None

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @property
    def email(self):
        return self.__email

    @username.setter
    def username(self, username):
        if Account.check_username(username) is False:
            raise Exception("invalid username")
        self.__username = username

    @password.setter
    def password(self, password):
        if Account.check_password(password) is False:
            raise Exception("invalid password")
        self.__password = hash(password)

    @email.setter
    def email(self, email):
        if Account.check_email(email) is False:
            raise Exception("invalid email")
        self.__email = email

    def show_welcome(self):
        first_name, last_name = self.username.split("_")
        first_name = first_name[0:1].upper() + first_name[1:]
        last_name = last_name[0:1].upper() + last_name[1:]
        username = first_name + " " + last_name
        if len(username) > 15:
            username = username[:15] + "..."
        return f"Welcome to our site {username}"

    def __eq__(self, other):
        return self.username == other.username \
            and self.email == other.email \
            and self.password == other.password


class Site:
    def __init__(self, url):
        self.__url = url
        self.__registered_users = []
        self.__active_users = []

    def register(self, account):
        if not isinstance(account, Account):
            raise TypeError
        if account in self.__registered_users:
            raise Exception("user already registered")
        self.__registered_users.append(account)
        return "register successful"

    def login(self, **kwargs):
        username, password, email = kwargs['username'], kwargs['password'], kwargs['email']
        if username and username in [account.username for account in self.__active_users]:
            return "user already logged in"
        if username and password:
            password = hash(kwargs['password'])
            for account in self.__registered_users:
                if account.username == username and account.password == password:
                    self.__active_users.append(account)
                    return "login successful"
        if username and password and email:
            try:
                account = Account(username, password, email)
                if account in self.__registered_users:
                    return "login successful"
            except:
                return "invalid login"
        else:
            raise Exception("invalid inputs")
        return "invalid login"

    def logout(self, username):
        if username in [account.username for account in self.__active_users]:
            self.__active_users.remove(username)
            return "logout successful"
        return "user is not logged in"
