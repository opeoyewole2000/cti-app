from django.conf.urls import  url, include
from . import views
from django.views.generic import ListView, DetailView
from .models import ctiRawTable




urlpatterns =[


url(r'^$', views.index, name='index'),
url(r'^analysis/$', views.analysis, name='analysis'),
url(r'^analysis/mod1/$', views.analysis_mod1,name='analysis_mod1'),

url(r'^analysis/mod2/$', views.analysis_mod2,name='analysis_mod2'),


url(r'^search/$', views.search, name='searchResults'),


url(r'^results/$', ListView.as_view(queryset=ctiRawTable.objects.all().order_by("-date")[:25],
                                    template_name="mainapp/results.html")),

# url(r'^results/(?P<pk>\d+)/', views.detailView.as_view(),name='resultsView'),

url(r'^results/(?P<pk>\d+)/', views.compare,name='resultsView'),

]





