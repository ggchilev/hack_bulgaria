from magic_reservation_system import Cinema


class Interface:


    def __init__(self, name):
        self._name = name

    def menu(self):
        print("Type 'show_movies' to see all the films !")
        print("Type 'show_movie_projections' to see the projections !")
        print("Type 'make_reservation' to make reservation !")
        print("Type exit to stop")

    def input(self, cinema):
        your_input = ""
        while your_input != "exit":
            self.menu()
            your_input = input("Type here> ")
            if your_input == "show_movies":
                cinema.show_movies()
            if your_input == 'show_movie_projections':
                movie_id = input("Type movie movie_id")
                cinema.show_movie_projections(movie_id)
            if your_input == 'make_reservation':
                cinema.make_reservation()


c = Cinema("Cinema")
i = Interface("Interface")
i.input(c)