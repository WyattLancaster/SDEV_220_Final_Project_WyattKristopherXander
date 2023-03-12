from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('register/', views.register, name='register'),
    path('login', views.user_login, name='login'),
    path('logout/', views.user_logout, name='lougout'),
    path('stjude/', views.stjude, name='stjude'),
    path('afa/', views.afa, name='afa'),
    path('riley/', views.riley, name='riley'),
    path('woundedwarrior/', views.woundedwarrior, name='woundedwarrior'),
    path('t2t/', views.t2t, name='t2t'),
    path('redcross/', views.redcross, name='redcross'),
    path('wwf/', views.wwf, name='wwf'),
    path('feedingamerica/', views.feedingamerica, name='feedingamerica'),
    path('ymca/', views.ymca, name='ymca'),
    path('donate/', views.donate, name='donate'),
]
