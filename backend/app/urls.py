from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/gerar_senha',views.gerar_senha,name="gerar_senha"),
    
 ]