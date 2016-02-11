from models import Client
from hashpass import hash_password


class ClientAlreadyRegistered(Exception):
    pass


class ClientNotFound(Exception):
    pass


class MainController:

    def register(self, email, password):
        user = self.session.query(Client).\
            filter(Client.email == email).first()

        if user is not None:
            raise ClientAlreadyRegistered('Client already registered')

        password, salt = hash_password(password, salt=None)
        client = Client(email=email, password=password, salt=salt)
        self.__commit_object(client)

    def login(self, email, password):
        user = self.session.query(Client).\
            filter(Client.email == email).\
            first()
        if user is None:
            print('kostana')
            raise ClientNotFound('There is no client with that username')
        password, salt = hash_password(password, user.salt)
        user = self.session.query(Client).\
            filter(Client.password == password).\
            first()
        if user is not None:
            return True

    def __commit(self):
        self.session.commit()

    def __commit_object(self, obj):
        self.session.add(obj)
        self.__commit()

    def __commit_objects(self, objects):
        self.session.add_all(objects)
        self.__commit()

    def __init__(self, session):
        self.session = session
