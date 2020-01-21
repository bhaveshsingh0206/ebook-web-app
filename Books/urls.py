from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<book_id>[0-9]+)$' , views.displayBook, name='displayBook'),
    url(r'^(?P<book_id>[0-9]+)/read/$' , views.readBook, name='readBook'),
    url(r'^(?P<book_id>[0-9]+)/addfavourite/$' , views.addfavourite, name='addfavourite'),
    url(r'^favourites/$', views.favourites, name='favourites'),
    url(r'^highrated/$', views.highrated, name='highrated'),
    url(r'^trending/$', views.trending, name='trending'),
    url(r'^editorchoice/$', views.editorchoice, name='editorchoice'),
url(r'^search/$', views.search, name='search'),
url(r'^horror/$', views.horror, name='horror'),
url(r'^Thriller/$', views.Thriller, name='Thriller'),
url(r'^Romantic/$', views.Romantic, name='Romantic'),
url(r'^Mystery/$', views.Mystery, name='Mystery'),
url(r'^Fiction/$', views.Fiction, name='Fiction'),
url(r'^Spiritual/$', views.Spiritual, name='Spiritual'),
url(r'^Psychology/$', views.Psychology, name='Psychology'),
url(r'^upload/$', views.upload, name='upload'),
url(r'^useruploads/$', views.useruploads, name='useruploads'),

    ]