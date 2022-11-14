from django.shortcuts import render
from django.views.generic import ListView

from books.models import Books


# Create your views here.


class BooksListView(ListView):
    model = Books
    template_name = 'list.html'