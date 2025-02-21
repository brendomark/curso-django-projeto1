#from receitas.views import home
from . import views

from django.urls import path


urlpatterns = [
    path('',views.home),
    path('receitas/<int:id>/',views.receitas),
   
]
