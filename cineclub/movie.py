import os
import json
import logging

LOGGER = logging.getLogger()

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data", "movies.json")

class Movie:
    def __init__(self, title: str) -> None:
        self.title = title.title()

    def __str__(self):
        return self.title

    def _get_movies(self):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)

    def _write_movies(self, movies):
        with open(DATA_FILE, 'w') as f:
            json.dump(movies, f, indent=4)

    def add_to_movies(self):
        liste_films = self._get_movies()
        if self.title not in liste_films:
            liste_films.append(self.title)
            self._write_movies(liste_films)
            return True
        else:
            LOGGER.warning(f"{self.title} est déjà dans la liste")
            return False

    def remove_from_movies(self):
        liste_films = self._get_movies()
        if self.title in liste_films:
            liste_films.remove(self.title)
            self._write_movies(liste_films)
            return True
        else:
            LOGGER.warning(f"{self.title} n'est pas dans la liste")
            return False

def get_movies():
    with open(DATA_FILE, 'r') as f:
        movies_title = json.load(f)
    return [Movie(movie) for movie in movies_title]

if __name__ == "__main__":
    movies = get_movies()
    for m in movies:
        print(m.title)