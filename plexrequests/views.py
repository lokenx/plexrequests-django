from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup
from pushbullet import Pushbullet


def search(request):
    return render(request, 'plexrequests/search.html')


def results(request):
    if 'q' in request.POST:
        q = request.POST['q']
        m_list = get_movies(q)
        i_list = get_imdb(q)
        if not m_list:
            return redirect('/')
        else:
            c_list = zip(m_list, i_list)
            return render(request, 'plexrequests/results.html',
                          {'list': c_list})
    else:
        return redirect('/')


def add(request):
    if 'movies' in request.POST:
        ma = request.POST['movies']
        am = add_to_cp(ma)
        return render(request, 'plexrequests/add.html',
                      {'a': am})
    else:
        return redirect('/')


def get_movies(search_for):
    url = "http://www.imdb.com/search/title?title_type=feature&title=" + search_for
    response = requests.get(url)
    movies_list = []
    for each_url in BeautifulSoup(response.text).select(".image"):
        movie_title = each_url.a.get('title')
        movies_list.append(movie_title)
    return movies_list


def get_imdb(search_for):
    url = "http://www.imdb.com/search/title?title_type=feature&title=" + search_for
    response = requests.get(url)
    movies_list = []
    for each_url in BeautifulSoup(response.text).select(".image"):
        movie_imdb = each_url.a.get('href')
        movies_list.append(movie_imdb)
    return movies_list


def add_to_cp(movie_req):
    cp_url="youripofcouchpotatowithport+apikey/"
    url2 = cp_url + "media.get/?id=" + movie_req
    cp_reg = requests.get(url2)
    cp_json = cp_reg.json()
    if cp_json['success'] is False:
        url3 = cp_url + "movie.add/?identifier=" + movie_req
        requests.post(url3)
        url4 = url2
        cp_reg2 = requests.get(url4)
        cp_json2 = cp_reg2.json()
        pb_key = Pushbullet("yourpushbulletapi")
        pb_key.push_note("Plex Request", cp_json2['media']['title'])
        cp = "true"
        return cp
    else:
        cp = "false"
        return cp
