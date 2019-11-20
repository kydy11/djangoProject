from django.urls import path
from .views import blog_post, add_comment

urlpatterns =[
    path('add', add_comment, name="add_comment"),
    path('get', blog_post, name="get_comment"),
]