from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path('', views.feed, name = "feed"),
    path('<int:blog_id>/', views.article, name="article"),
    path('writer/<int:blogger_id>/', views.writer, name="writer"),
]