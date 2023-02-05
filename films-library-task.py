print("Biblioteka filmów")


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
    def __str__(self):
        return f"{title} ({publication_year})"

class Serial(PlayFunction):
    def __init__(self, title, publication_year, genre, s_number, e_number, views):
        self.title = title
        self.publication_year = publication_year
        self.genre = genre
        self.e_number = e_number
        self.s_number = s_number
        self.views = views
    def __str__(self):
        return f"{title} S{s_number:02}E{e_number:02}"

movies_list = [
    ["Pulp Fiction", "1994", "crime", "14"],
    ["Forrest Gump", "1994", "drama", "100"],
    ["Matrix", "1999", "action", "299"],
    ["Gladatior", "2000", "action", "399"],
    ["The Simpsons", "1989", "comedy", "1", "2", "1989"],


]

get_movies = []
get_series = []

for i in range(0, len(movies_list)):
    if len(movies_list[i]) == 4:
        get_movies.append(movies_list[i])
    else: get_series.append(movies_list[i])

get_movies = sorted(get_movies, key=lambda j: j.title)
get_series = sorted(get_series, key=lambda k: k.title)
print(get_movies)
print(get_series)

#print(movies_list[1][3])
print(len(movies_list))