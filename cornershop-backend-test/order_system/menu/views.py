# Django Imports
from rest_framework.generics import RetrieveUpdateDestroyAPIView, \
    ListCreateAPIView
from rest_framework.status import HTTP_201_CREATED
from order_system.menu.models import Menu, Ingredients
from order_system.menu.serializers import MenuModelSerializer, \
    IngredientModelSerializer


class MenuAPIView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    """Menu Api view"""
    queryset = Menu.objects.all()
    serializer_class = MenuModelSerializer


class IngredientsGetCreateAPIView(ListCreateAPIView):
    """Ingredients Api view"""
    queryset = Ingredients.objects.all()
    serializer_class = IngredientModelSerializer


class IngredientsAPIView(RetrieveUpdateDestroyAPIView):
    """Ingredients Api view"""
    queryset = Ingredients.objects.all()
    serializer_class = IngredientModelSerializer
    lookup_field = 'pk'
