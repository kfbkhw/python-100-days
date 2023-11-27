from bs4 import BeautifulSoup
import requests

webpage = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/").text
soup = BeautifulSoup(webpage, "html.parser")

movie_title = soup.find_all(name="h3", class_="title")
movie_list = [movie.text for movie in movie_title]
movie_list.reverse()

with open("movies.txt", "w") as file:
    for movie in movie_list:
        file.write(f"{movie}\n")
