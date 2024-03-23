from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path('kisses/', views.kisses,name="kisses"),
    path('nudes/', views.nudes,name="nudes"),
    path('date/', views.date,name="date"),
    path('logout/', views.custom_logout, name='logout'),
    path('updatedate/', views.updatedate, name='updatedate'),
    path('update-next-date/', views.update_next_date, name='update_next_date'),
    path('update-last-date/', views.update_last_date, name='update_last_date'),
    path('update_dates/', views.update_dates, name='update_dates'),
    path('update_both/', views.update_both, name='update_both'),
    path('send-kiss/', views.send_kiss, name='send_kiss'),
    path('kiss_send/', views.kiss_send, name='kiss_send'),
    path('send_nude/', views.send_nude, name='send_nude'),
    path('nude_sent/', views.nude_sent, name='nude_sent'),
    path('see-nudes/', views.view_kiss_images, name='view_kiss_images'),
    path('messages/', views.view_kiss_messages, name='view_kiss_messages'),
    path('',include('django.contrib.auth.urls')),

]