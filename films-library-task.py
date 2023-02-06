class Movie():
    def __init__(self, title, publication_year, genre, views):
        self.title = title
        self.publication_year = publication_year
        self.genre = genre
        self.views = views

    def play(self, new_view = 1):
        self.views += new_view

    def __str__(self, *args, **kwargs):
        return f"{self.title} ({self.publication_year})"

import random

from faker import Faker
fake = Faker()

list_of_movies = []
list_of_movies.append(Movie(title="Pulp Fiction", publication_year=1994, genre="crime", views=0))
list_of_movies.append(Movie(title="Forrest Gump", publication_year=1994, genre="drama", views=0))
list_of_movies.append(Movie(title="Matrix", publication_year=1999, genre="action", views=0))
list_of_movies.append(Movie(title="Gladiator", publication_year=2000, genre="action", views=0))

for i in range(1, 10):
    list_of_movies.append(Movie(title=fake.company(), publication_year=random.randint(1950, 2023), genre="comedy", views=0))

class Serial():
    def __init__(self, title, publication_year, genre, s_number, e_number, views):
        self.title = title
        self.publication_year = publication_year
        self.genre = genre
        self.e_number = e_number
        self.s_number = s_number
        self.views = views

    def play(self, new_view = 1):
        self.views += new_view

    def __str__(self, *args, **kwargs):
        return f"{self.title} S{self.s_number:02}E{self.e_number:02}"
        #return f"{self.title} S{self.s_number:02}E{self.e_number:02}"

list_of_movies.append(Serial(title="The Simpsons", publication_year=1989, genre="comedy", s_number=1, e_number=2, views=0))
list_of_movies.append(Serial(title="The Simpsons", publication_year=1989, genre="comedy", s_number=1, e_number=1, views=0))

for i in range(1, 7):
    list_of_movies.append(Serial(title=fake.company(), publication_year=random.randint(1950, 2023), genre="comedy", s_number=1, e_number=i, views=0))


class FinalLibrary(Movie, Serial):
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
    print("")
    print("Lista filmów (uporządkowane alfabetycznie):")
    for i in range(0,len(get_movies_list)):
        print(get_movies_list[i])
get_movies()

def get_series():
    print("")
    print("Lista seriali (uporządkowane alfabetycznie):")
    for i in range(0, len(get_series_list)):
        print(get_series_list[i])    
get_series()

print("")
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

random_movie = 0
random_additional_views = 0
print("")
print("Po zliczeniu odtworzeń filmów:")
def generate_views():
    random_movie = random.randint(0, len(list_of_movies) - 1)
    random_additional_views = random.randint(0, 100)
    list_of_movies[random_movie].views += random_additional_views
    print(list_of_movies[random_movie], "liczba odsłon: ", list_of_movies[random_movie].views, ", z czego dodano: ", random_additional_views)
generate_views()

def generate_views_multi():
    for i in range(1, 10):
        generate_views()
generate_views_multi()

popular_movies_sorted = []

from datetime import datetime
max_ranking_list = 0
def top_titles():
    print(" ")
    popular_movies = int(input("Ile najpopularniejszych tytułów z Biblioteki filmów podać? "))
    popular_movies_sorted = sorted(list_of_movies, key=lambda j: j.views, reverse=True)

    if popular_movies <= len(list_of_movies):
        max_ranking_list = popular_movies
    else:
        max_ranking_list = len(list_of_movies)

    print("Najpopularniejsze filmy i seriale dnia", datetime.today().strftime('%d.%m.%Y.'), "to: ")
    
    for i in range(0, max_ranking_list):
        print(popular_movies_sorted[i], "-> ilość wyświetleń:", popular_movies_sorted[i].views)

top_titles()