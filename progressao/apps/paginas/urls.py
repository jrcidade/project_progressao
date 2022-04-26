from django.urls import path
from progressao.apps.paginas import views

urlpatterns = [
    path('home/', views.home),
]