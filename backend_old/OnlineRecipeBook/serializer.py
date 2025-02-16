from rest_framework import serializers
from OnlineRecipeBook.users.models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['name', 'category']