from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    path('', views.PostListView.as_view()),
    path('<int:pk>/', views.CommentList.as_view()),
    path('profile/<int:pk>/', views.PostList.as_view()),
    path('create/', views.PostCreateView.as_view()),
    path('like/<int:pk>/', views.PostLikeView.as_view()),
    path('rating/<int:pk>/', views.PostRateViewSet.as_view()),
]
