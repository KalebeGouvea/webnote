from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path ('', views.index, name='index'),
    path ('add/', views.adicionar, name='adicionar'),
    path ('<int:nota_id>/ver/', views.visualizar, name='visualizar'),
    path ('enviar/', views.envianota, name='envianota'),
    path ('<int:nota_id>/editar/', views.editanota, name='editanota'),
    path ('<int:nota_id>/deletar/', views.deletanota, name='deletanota'),
]