from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CartDownload, CartViewSet, CreateUserViewSet,
                    FavoriteViewSet, IngredientViewSet, RecipeViewSet,
                    SubscribeViewSet, TagViewSet)

router_v1 = DefaultRouter()

router_v1.register('users', CreateUserViewSet, basename='users')
router_v1.register(r'tags', TagViewSet, basename='tags')
router_v1.register(r'recipes', RecipeViewSet, basename='recipes')
router_v1.register(r'ingredients', IngredientViewSet, basename='ingredients')

urlpatterns = [
    path('users/subscriptions/',
         SubscribeViewSet.as_view({'get': 'list'}), name='subscriptions'),
    path('recipes/download_shopping_cart/',
         CartDownload.as_view({'get': 'download'}), name='download'),
    path('users/<users_id>/subscribe/',
         SubscribeViewSet.as_view({'post': 'create',
                                   'delete': 'delete'}), name='subscribe'),
    path('recipes/<recipes_id>/favorite/',
         FavoriteViewSet.as_view({'post': 'create',
                                  'delete': 'delete'}), name='favorite'),
    path('recipes/<recipes_id>/shopping_cart/',
         CartViewSet.as_view({'post': 'create',
                              'delete': 'delete'}), name='cart'),
    path('', include(router_v1.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]
