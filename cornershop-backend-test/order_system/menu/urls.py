from django.urls import path
from order_system.menu.views import MenuAPIView, IngredientsGetCreateAPIView, \
    IngredientsAPIView


urlpatterns = [
    path('menu/', MenuAPIView.as_view(), name='menu_create'),
    path('menu/<int:id>', MenuAPIView.as_view(), name='menu_get_put_patch'),
    path('ingredients/', IngredientsGetCreateAPIView.as_view()),
    path('ingredients/<str:pk>/', IngredientsAPIView.as_view()),
]
