import sqlite3


class Cinema:

    def __init__(self, name):
        self._name = name

    def add_movie(self, movie):
        if movie not in movies:
            movies.append(movie)

    def connect_to_db(self):
        conn = sqlite3.connect('Cinema')
        return conn

    def show_movies(self):
        conn = self.connect_to_db()
        c = conn.cursor()
        all_movies = c.execute("SELECT * FROM movies order by rating")
        for item in all_movies:
            print(item)
        conn.commit()
        conn.close()

        return all_movies

    def free_places(self):
        my_dic = {}
        conn = self.connect_to_db()
        c = conn.cursor()
        projections = c.execute("SELECT projection_id FROM reservations")
        for item in projections:
            if item[0] not in my_dic:
                my_dic[item[0]] = 1
            else:
                my_dic[item[0]] += 1

        return my_dic

    def show_movie_projections(self, movie_id):
        my_dic = self.free_places()
        free_places_dic = {}
        conn = self.connect_to_db()
        c = conn.cursor()
        projections = c.execute(
            "SELECT * FROM projections where movie_id = ? order by date ", movie_id)
        for item in projections:
            if item[0] in my_dic:
                free_places_dic[item[0]] = 100 - my_dic[item[0]]
            else:
                free_places_dic[item[0]] = 100
            print(item, " - ", free_places_dic[item[0]], "free places")
        conn.commit()
        conn.close()

        return free_places_dic

    def insert_reservations(self, my_list):
        conn = self.connect_to_db()
        c = conn.cursor()
        c.execute("""INSERT INTO Reservations (id, username, projection_id, row, col)
                     VALUES(?, ?, ?, ?, ?)
                     """,my_list)
        conn.commit()
        conn.close()

    def show_screen(self, rows_and_cols):
        h = 0
        screen_matrix = [["." for x in range(10)] for x in range(10)]
        for row in range(0, len(screen_matrix)):
            for col in range(0, len(screen_matrix)):
                for item in rows_and_cols:
                    if row == item[0] and col == item[1]:
                        screen_matrix[row][col] = "X"
        return screen_matrix

    def get_rows_and_cols(self, projection_id):
        conn = self.connect_to_db()
        c = conn.cursor()
        taken_places_list = []
        rows_and_cols = c.execute(
            "SELECT row,col FROM reservations where projection_id = ? ", projection_id)
        for item in rows_and_cols:
            taken_places_list.append(item)
        return taken_places_list


    def your_movie(self, movie_id):
        conn = self.connect_to_db()
        c = conn.cursor()
        movie_name = c.execute(
            "SELECT name FROM movies where id = ? ", movie_id)
        return movie_name

    def finilize(self):
        finilize = input("To confirm type 'finilize'")
        if finilize == 'finilize':
            return True
        else:
            return False

    def reservation_list(self, id, name, proj_id, row, col):
        reservation_list = [id, name, proj_id, row, col]
        return reservation_list

    def select_last_id_from_reservations(self):
        conn = self.connect_to_db()
        c = conn.cursor()
        ids = c.execute("SELECT id FROM reservations")
        last = (0,)
        for item in ids:
            last = item
        return last[0]




    def make_reservation(self):
        is_reserved = False
        my_places = []
        name = input("Choose name> ")
        tickets = input("Choose number of tickets> ")
        print("Here are the films: ")
        self.show_movies()
        movie_id = input("Choose a movie> ")
        projection_dic = self.show_movie_projections(movie_id)
        projection = input("Choose projection> ")
        if projection_dic[int(projection)] < int(tickets):
            return False
        taken_places_list = self.get_rows_and_cols(projection)
        screen = self.show_screen(taken_places_list)
        for item in screen:
            print(item)
        for index in range(0, int(tickets)):
            is_reserved = False
            while is_reserved == False:
                seat = input("Choose seat " + str(index + 1))
                lis = seat.split(",")
                tup = (int((lis[0])[1]), int((lis[1])[0]))
                if not isinstance(tup, tuple):
                    raise ValueError
                if (tup[0] < 0 or tup[0] >= 10) or (tup[1] < 0 or tup[1] >= 10):
                    print("Lol....NO!")
                else:
                    if screen[tup[0]][tup[1]] == ".":
                        screen[tup[0]][tup[1]] = "X"
                        tup2 = (tup[0], tup[1])
                        my_places.append(tup2)
                        reservation_list = self.reservation_list(self.select_last_id_from_reservations()+1, name, projection, tup[0], tup[1])
                        self.insert_reservations(reservation_list)
                        reservation_list = []
                        is_reserved = True
                    else:
                        print("This seat is already taken")
        print("This is your reservation: ")
        movie = self.your_movie(movie_id)
        print("Your movie : ")
        for item in movie:
            print(item)
        print("Your seats :")
        for item in my_places:
            print(item)
        return self.finilize()
