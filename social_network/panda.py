class Panda:

    def __init__(self, name, email, gender):
        self._name = name
        self._email = email
        self._gender = gender

        self.friend_list = set()

    def __str__(self):
        return 'Panda ' + self._name

    def __hash__(self):
        return 2

    def __eq__(self, other):
        if self._name == other._name and self._email == other._email and self._gender == other._gender:
            return True
        else:
            return False

    def get_name(self):
        return self._name

    def get_gender(self):
        return self._gender

