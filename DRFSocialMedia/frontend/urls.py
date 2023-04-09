from django.urls import path
from .views import home, comments_page, profile_page, settings_page, followers_page, following_page

app_name = 'frontend'

urlpatterns = [
    path('', home, name='home'),
    path('settings/', settings_page, name='settings'),
    path('profile/<int:id>/', profile_page, name='profile'),
    path('post/<int:id>/comments/', comments_page, name='comments'),
    path('following/<int:id>/', following_page, name='following'),
    path('followers/<int:id>/', followers_page, name='followers'),
]