from django.urls import path

from produtos import views


urlpatterns = [
    path('produtos/<int:pk>/', views.ProdutosAPI.as_view()),
    path('produtos/', views.ProdutosList.as_view()),
]
