from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home, name="home"),
    path('details/<int:id>/', views.detail, name="detail"),
    path('addbooks/', views.add_books, name="add_books"),
    path('editbooks/<int:id>/', views.edit_books, name="edit_books"),
    path('deletebooks/<int:id>', views.delete_books, name="delete_book"),
]
