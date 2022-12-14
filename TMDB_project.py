all_movie = []
base_url = "https://www.themoviedb.org/movie?page="
common_url = "https://www.themoviedb.org"
url_list = []
for x in range(1,51):
    url_list.append(base_url+str(x))
import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
for url in url_list:
    page_data = requests.get(url,headers=headers).text
    soup_page = BeautifulSoup(page_data,"lxml")
    all_divs = soup_page.find_all("div",class_="card style_1")
    for div in all_divs:
        movie_name = div.find("a")["title"]
        import datetime as dt
        r_date = dt.datetime.strptime(div.find("p").text, "%b %d, %Y")
        release_date = f'{r_date.month}/{r_date.day}/{r_date.year}'
        movie_url = div.find("a")["href"]
        movie_url = (common_url+movie_url)
        movie_data = requests.get(movie_url,headers=headers).text
        soup_movie = BeautifulSoup(movie_data,"lxml")
        ratings = soup_movie.find("div",class_="user_score_chart")["data-percent"]
        genres = soup_movie.find("span",class_="genres").text
        if genres.isspace():
            genres = "N/A"
        else:
            genres = genres
        try:
            time = soup_movie.find("span",class_="runtime").text
        except:
            time = "N/A"
        cast = soup_movie.find_all("li",class_="profile")
        for character in cast:
            post = character.find("p",class_="character").text
            if "Director" in post:
                name= character.find('p').text
        all_movie_info ={
            "Name":movie_name,
            "Rating":ratings,
            "Genre":genres.strip(),
            "Release date":release_date,
            "Runtime":time.strip(),
            'Director' : name,
            "Url":movie_url
            }
        all_movie.append(all_movie_info)

import pandas
mf = pandas.DataFrame(all_movie)
print(mf)
mf.to_excel('all_movie.xlsx')