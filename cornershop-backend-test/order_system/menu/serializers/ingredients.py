from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from order_system.menu.models import Ingredients


class IngredientModelSerializer(serializers.Serializer):
    """Ingredient model serializer"""

    id = serializers.UUIDField(required=False)
    name = serializers.CharField(
        validators=[UniqueValidator(queryset=Ingredients.objects.all())],
        max_length=150,
        min_length=6
    )
    description = serializers.CharField(
        max_length=255, min_length=10,
        allow_null=True, allow_blank=True,
        required=False
    )
    is_active = serializers.BooleanField(default=True)

    def create(self, validated_data):
        """Handle user creation"""

        ingredient = Ingredients.objects.create(**validated_data)
        return ingredient

    def update(self, instance, validated_data):
        """Handle user creation"""

        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance
