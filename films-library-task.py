class PlayFunction:
    def __init__(self, new_view = 1):
        self.new_view = new_view
        self.views += new_view

class Movie(PlayFunction):
    def __init__(self, title, publication_year, genre, views):
        self.title = title
        self.publication_year = publication_year
        self.genre = genre
        self.views = views
    def __str__(self, *args, **kwargs):
        return f"{self.title} ({self.publication_year})"

list_of_movies = []
list_of_movies.append(Movie(title="Pulp Fiction", publication_year=1994, genre="crime", views=14))
list_of_movies.append(Movie(title="Forrest Gump", publication_year=1994, genre="drama", views=100))
list_of_movies.append(Movie(title="Matrix", publication_year=1999, genre="action", views=299))
list_of_movies.append(Movie(title="Gladiator", publication_year=2000, genre="action", views=399))


class Serial(PlayFunction):
    def __init__(self, title, publication_year, genre, s_number, e_number, views):
        self.title = title
        self.publication_year = publication_year
        self.genre = genre
        self.e_number = e_number
        self.s_number = s_number
        self.views = views
    def __str__(self, *args, **kwargs):
        return f"{self.title} S{self.s_number:02}E{self.e_number:02}"
        #return f"{self.title} S{self.s_number:02}E{self.e_number:02}"

list_of_movies.append(Serial(title="The Simpsons", publication_year=1989, genre="comedy", s_number=1, e_number=2, views=198))
list_of_movies.append(Serial(title="The Simpsons", publication_year=1989, genre="comedy", s_number=1, e_number=1, views=192))


class FinalLibrary(Movie, Serial, PlayFunction):
    print("Biblioteka filmów")

    def __init__(self):
        self.list = []

    def __len__(self):
        return len(self.list)

get_movies_list = []
get_series_list = []


for i in range(0, len(list_of_movies)):
    try: 
        list_of_movies[i].s_number * 0 != 0
        get_series_list.append(list_of_movies[i])
    except AttributeError:
        get_movies_list.append(list_of_movies[i])

get_movies_list = sorted(get_movies_list, key=lambda j: j.title)
get_series_list = sorted(get_series_list, key=lambda k: k.title) #wpierw porządkowanie po nazwie
get_series_list = sorted(get_series_list, key=lambda k: k.s_number) #potem porządkowanie po nr serii
get_series_list = sorted(get_series_list, key=lambda k: k.e_number) #na koniec porządkowanie po nr epizodu / odcinka

def get_movies():
    for i in range(0,len(get_movies_list)):
        print(get_movies_list[i])

def get_series():
    for i in range(0, len(get_series_list)):
        print(get_series_list[i])    

get_movies()
get_series()


title_of_movie = str(input("Jeśli chcesz sprawdzić czy poszukiwany przez Ciebie film występuje w Bibliotece filmów, to podaj nazwę: "))
no_of_movie = None
def search(some_title):
    for i in range(0, len(list_of_movies)):
        if list_of_movies[i].title == some_title:
            no_of_movie = i
            pass
        else: 
            pass
   
    try:
        no_of_movie >= 0
        print("Film '" + list_of_movies[no_of_movie].title + "' jest w Bibliotece filmów")
    except UnboundLocalError:
        print("Film '" + title_of_movie + "' nie znajduje się w Bibliotece filmów")
search(title_of_movie)
