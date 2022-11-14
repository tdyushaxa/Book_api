from django.urls import path

from api.views import BookAPiView

urlpatterns=[
    path('',BookAPiView.as_view())
]