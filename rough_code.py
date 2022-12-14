# all_movie = []
# base_url = "https://www.themoviedb.org/movie?page="
# common_url = "https://www.themoviedb.org"
# url_list = []
# # movieurl_lst = []
# for x in range(1,51):
#     url_list.append(base_url+str(x))
# # print(url_list)
# import requests
# from bs4 import BeautifulSoup
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
# for url in url_list:
#     page_data = requests.get(url,headers=headers).text
#     soup_page = BeautifulSoup(page_data,"lxml")
#     # print(soup_page)
#     all_divs = soup_page.find_all("div",class_="card style_1")
#     # print(all_divs)
#     for div in all_divs:
#         movie_name = div.find("a")["title"]
#         # print(movie_name)
#         import datetime as dt
#         r_date = dt.datetime.strptime(div.find("p").text, "%b %d, %Y")
#         release_date = f'{r_date.month}/{r_date.day}/{r_date.year}'
#         # print(release_date)
#         movie_url = div.find("a")["href"]
#         # print(movie_url)
#         movie_url = (common_url+movie_url)
#         # print(movie_url)
#         # movieurl_lst.append(movie_url)
#         # for movieurl in movieurl_lst:
#         movie_data = requests.get(movie_url,headers=headers).text
#         soup_movie = BeautifulSoup(movie_data,"lxml")
#         ratings = soup_movie.find("div",class_="user_score_chart")["data-percent"]
#         # print(ratings)
#         genres = soup_movie.find("span",class_="genres").text
#         # print(type(genre))
#         if genres.isspace():
#             genres = "N/A"
#         else:
#             genres = genres
#         # print(genres.strip())
#         try:
#             time = soup_movie.find("span",class_="runtime").text
#         except:
#             time = "N/A"
#         # print(time.strip())
#         cast = soup_movie.find_all("li",class_="profile")
#         # print(cast)
#         for character in cast:
#             post = character.find("p",class_="character").text
#             # print(post)
#             if "Director" in post:
#                 name= character.find('p').text
#                 # print(name)
#         all_movie_info ={
#             "Name":movie_name,
#             "Rating":ratings,
#             "Genre":genres.strip(),
#             "Release date":release_date,
#             "Runtime":time.strip(),
#             'Director' : director,
#             "Url":movie_url
#             }
#         all_movie.append(all_movie_info)
# # print(all_movie)
# import pandas
# mf = pandas.DataFrame(all_movie)
# print(mf)
# mf.to_excel('all_movie.xlsx')