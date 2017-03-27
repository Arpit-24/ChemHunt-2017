from django.conf.urls import url, include
from .import views


app_name = 'chemhunt'

urlpatterns = [

    url(r'^test/$', views.test, name='test'),

    url(r'^$', views.main, name='main'),

    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),

    url(r'^(?P<pk>[0-9]+)/answer/$', views.answer, name='answer'),

    url(r'^(?P<pk>[0-9]+)/skip/$', views.skip, name='skip'),

    url(r'^main/$', views.main, name='main'),

    url(r'^index/$', views.index, name='index'),




            ]
