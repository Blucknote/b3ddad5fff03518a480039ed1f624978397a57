from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.chart_rows, name='chart_rows'),
    url(r'^crow/add/$', views.crow_add, name='crow_add'),
]
