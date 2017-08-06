"""django_IMDB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from movies.views import search_movies, home, get_watchlist, add_in_watchlist, movie_details
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^admin/', admin.site.urls, name="admin"),
    url(r'^$', login_required(home, login_url='/login/'), name="home"),
    url(r'^search_movie/$', login_required(search_movies, login_url='/login/'), name="search_movie"),
    url(r'^add_in_watchlist/$', login_required(add_in_watchlist, login_url='/login/'), name="add_in_watchlist"),
    url(r'^watchlist/$', login_required(get_watchlist, login_url='/login/'), name="watchlist"),
    url(r'^details/$', login_required(movie_details, login_url='/login/'), name="movie_details"),
    url(r'^login/$', auth_views.login, name="login"),
    url(r'^logout/$', auth_views.logout),

]
