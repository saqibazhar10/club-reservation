from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path("", views.homepage ,name="homepage"),
    path("login/", views.login ,name="login"),
    path("logout/", views.logout ,name="logout"),
    path("reg/", views.register ,name="register"),
    path("confirm/", views.confirm ,name="confirm"),
    path("Manager/", views.Manage_Page ,name="Manager"),
    path("membership/", views.membership ,name="membership"),
    path("feedback/", views.feed_back ,name="feedback"),
    path("reservation/", views.reservation ,name="reservation"),
    path("payment/", views.payment ,name="payment"),
    path("history/", views.history ,name="history"),

    path('chat/', views.chat, name='chat'),
    path('<str:room>/', views.room, name='room'),
    path('chat/checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    
    

]