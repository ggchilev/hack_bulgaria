from controllers import ClientAlreadyRegistered, ClientNotFound
import getpass


class MainView:
    def __init__(self, controller):
        self.controller = controller

    def render(self):
        while True:
            command = input('Enter command>')

            if command == 'register':
                email = input('Email:')
                password = getpass.getpass('Password:')

                try:
                    self.controller.register(email, password)
                    print('Success!')
                except ClientAlreadyRegistered as e:
                    print(e)

            elif command == 'login':
                email = input('Email:')
                password = getpass.getpass('Password:')
                try:
                    if self.controller.login(email, password) is True:
                        print('Welcome')
                    else:
                        print('Wrong password')
                except ClientNotFound as e:
                    print(e)

            else:
                print("Wrong command")
