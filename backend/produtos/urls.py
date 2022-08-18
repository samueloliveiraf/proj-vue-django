from django.urls import path

from produtos import views


urlpatterns = [
    path('api/<int:pk>/', views.ProdutosAPI.as_view()),
    path('api/', views.ProdutosList.as_view()),
]
