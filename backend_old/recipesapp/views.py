from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from recipesapp.models import Recipe  # Import your model
from recipesapp.serializer import RecipeSerializer


class RecipeUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)  # Allows file uploads

    def post(self, request, *args, **kwargs):
        """Handles recipe creation"""
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        """Handles retrieving all recipes"""
        recipes = Recipe.objects.all()  # Get all recipes from DB
        serializer = RecipeSerializer(recipes, many=True)  # Serialize the data
        return Response(serializer.data, status=status.HTTP_200_OK)  # Return JSON response



class RecipeSearchView(ListAPIView):
    """Search for a recipe by name and return its details"""
    serializer_class = RecipeSerializer

    def get_queryset(self):
        name = self.kwargs.get("name", None)  # Use .get() to prevent KeyError

        if name:
            print("SEARCH PASSED!")
            return Recipe.objects.filter(name__icontains=name)
        else:
            print("SEARCH FAILED!")
            return Recipe.objects.all()


class IncreaseLikesView(APIView):
    """Increase likes for a recipe"""

    def post(self, request, *args, **kwargs):
        recipe_name = self.kwargs["name"]
        try:
            recipe = Recipe.objects.get(name=recipe_name)
            recipe.no_of_likes += 1  # Increase by 1
            recipe.save()
            return Response({"message": "Likes updated", "no_of_likes": recipe.no_of_likes}, status=status.HTTP_200_OK)
        except Recipe.DoesNotExist:
            return Response({"error": "Recipe not found"}, status=status.HTTP_404_NOT_FOUND)

