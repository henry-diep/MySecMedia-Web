from django.urls import include, re_path
from django.urls import path

from . import views

urlpatterns = [    
    path('',views.index,name='index'),
    path('home',views.RSSList.as_view(),name='listview'),
    path('rss',views.rss,name='rss'),
    path('about',views.about,name='about'),    
    path('acsm',views.acsm,name='acsm'),
    path('asm',views.asm,name='asm'),
    path('apsm',views.apsm,name='apsm'),
    path('cctv',views.cctv_view,name='cctv'),
    path('space',views.space_view,name='space'),
    path('crl',views.crl_view,name='crl'),
    path('chiefit',views.chiefit_view,name='chiefit'),
    path('smartcities',views.smartcities_view,name='smartcities'),
    path('drastic',views.drastic_view,name='drastic'),
    path('asean',views.asean_view,name='asean'),   
    path('test',views.test_view,name='test'),
    path('msmall',views.msmall,name='msmall'),
    path('load',views.load,name='load'),
    path('update',views.load,name='update'),
    path('',views.RSSList.as_view(),name='listview'),
    path('optout',views.optout,name='optout'),
    path('hello', views.year_archive,name='hello'),
    path('newsletter', views.newsletter, name='newsletter')
]
