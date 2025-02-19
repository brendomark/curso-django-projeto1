from receitas.views import home, sobre, contato
from django.urls import path


urlpatterns = [
    path('',home),
    path('sobre/',sobre),
    path('contato',contato),
]
