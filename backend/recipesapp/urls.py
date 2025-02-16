from tkinter.font import names

from django.urls import path

import recipesapp.views
from .views import RecipeUploadView, RecipeSearchView, IncreaseLikesView

urlpatterns = [
    path('upload/', RecipeUploadView.as_view(), name='recipe-upload'),
    path('retrieve-all/', RecipeUploadView.as_view(), name='retrieve-recipes'),
    path('search/<str:name>/', RecipeSearchView.as_view(), name='recipe-search'),
    path('<str:name>/like/', IncreaseLikesView.as_view(), name='increase-likes'),
]

# urlpatterns+=