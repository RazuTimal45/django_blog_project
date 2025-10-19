from django.urls import path
from .import views

urlpatterns = [
    path('blog',views.post_list, name='post_list'),
    path('blog/create/', views.post_create, name='post_create'),
    path('blog/update/<int:pk>/',views.post_update, name='post_update'),
    path('blog/delete/<int:pk>/',views.post_delete, name='post_delete'),
]
