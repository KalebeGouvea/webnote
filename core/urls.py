from django.urls import path, include

from . import views

app_name = 'core'
urlpatterns = [
    path ('', views.index, name='index'),
    #path ('login/', views.login, name='login'),
    path ('envialogin/', views.envialogin, name='envialogin'),
    path ('cadastrar/', views.cadastrar, name='cadastrar'),
    path ('enviacadastro/', views.enviacadastro, name='enviacadastro'),
    path ('add/', views.adicionar, name='adicionar'),
    path ('<int:nota_id>/ver/', views.visualizar, name='visualizar'),
    path ('enviar/', views.envianota, name='envianota'),
    path ('<int:nota_id>/editar/', views.editanota, name='editanota'),
    path ('<int:nota_id>/deletar/', views.deletanota, name='deletanota'),
    path ('sobre/', views.sobre, name='sobre'),
    path('accounts/', include('django.contrib.auth.urls')),
]