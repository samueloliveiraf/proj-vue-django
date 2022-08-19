from django.urls import path

from funcionarios import views


urlpatterns = [
    path('funcionarios/<int:pk>/', views.FuncionariosCrud.as_view()),
    path('funcionarios/', views.FuncionariosListPost.as_view()),
]
