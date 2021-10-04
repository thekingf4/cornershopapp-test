# django Imports
from django.db.models import CharField, BooleanField, UUIDField, ForeignKey, \
    CASCADE, Model
# Utils imports
from uuid import uuid4
from order_system.utils.models import MetaDataInfo


class Menu(MetaDataInfo, Model):
    """Menus model

    Menu created to store the name of each dish that is offered, additionally
    it has the following attributes:
    id (UUIDField): Store the pk id when the object was created
    name (CharField): Store the name when the object was created
    description (CharField): Store when the description(optional) the object was
    created
    is_active: Store the is_active when the object was created
    """
    id = UUIDField(primary_key=True, default=uuid4, editable=False)
    name = CharField(max_length=150)
    description = CharField(max_length=255, blank=True, null=True)
    is_active = BooleanField(default=True)

    def __str__(self):
        return self.name


class Ingredients(MetaDataInfo, Model):
    """Ingredient model


    created to store the ingredients that each dish will carry, it has the
    following attributes:
    id (UUIDField): Store the pk id when the object was created
    name (CharField): Store the name when the object was created
    description (CharField): Store when the description(optional) the object was
    created
    is_active: Store the is_active when the object was created
    """
    id = UUIDField(primary_key=True, default=uuid4, editable=False)
    name = CharField(max_length=150)
    description = CharField(max_length=255, blank=True, null=True)
    is_active = BooleanField(default=True)

    def __str__(self):
        return self.name


class DetailMenu(Model):
    """DetailMenu model

    Created to relate the creation of each dish with its ingredients, it has
    the following attributes:
    ingredient (ForeignKey): Store the ingredient when the object was created
    menu (ForeignKey): Store the menu when the object was created
    """
    ingredient = ForeignKey(Ingredients, on_delete=CASCADE)
    menu = ForeignKey(Menu, on_delete=CASCADE)
