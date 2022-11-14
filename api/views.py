from rest_framework.generics import ListAPIView

from api.serializers import BooksSerializers
from books.models import Books


# Create your views here.

class BookAPiView(ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializers


