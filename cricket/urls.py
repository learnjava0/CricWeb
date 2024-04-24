from django.contrib import admin
from django.urls import path
from cricket import views

urlpatterns = [
    path('', views.index, name='cricket'),
    path('index', views.index, name='index'),
    path("stats", views.stats, name='stats'),
    path("teams", views.teams, name='teams'),
    path("pointtable", views.pointtable, name='pointtable'),
    path("contact", views.contact, name='contact'),
    path("csk",views.csk, name="csk"),
    path("dc",views.dc, name="dc"),
    path("gt",views.gt, name="gt"),
    path("kkr",views.kkr, name="kkr"),
    path("lsg",views.lsg, name="lsg"),
    path("mi",views.mi, name="mi"),
    path("punjab",views.punjab, name="punjab"),
    path("rr",views.rr, name="rr"),
    path("rcb",views.rcb, name="rcb"),
    path("srh",views.srh, name="srh"),


]
