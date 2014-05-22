from django.conf.urls import patterns, url

from app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^addsheet$', views.addsheet, name='addsheet'),
    url(r'^allsheets$', views.allsheets, name='allsheets')
)