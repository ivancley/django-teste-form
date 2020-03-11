from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePergunta),
    path('formulario', views.formularioPergunta),
    path('feedback', views.feedback)
]
