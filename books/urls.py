from django.urls import path

from books.views import BooksListView

urlpatterns = [
    path('',BooksListView.as_view(),name='list')
]