from django.contrib import admin
from foodgram.settings import EMPTY_VALUE
from users.models import User

from .models import (Cart, FavoriteRecipe, Ingredient, IngredientRecipe,
                     Recipe, Subscribe, Tag, TagRecipe)


class IngredientRecipeInline(admin.TabularInline):
    model = IngredientRecipe
    extra = 0


class TagRecipeInline(admin.TabularInline):
    model = TagRecipe
    extra = 0


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'id', )
    search_fields = ('username', 'email', )
    empty_value_display = EMPTY_VALUE
    list_filter = ('username', 'email', )


@admin.register(Ingredient)
class IngrAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit', )
    search_fields = ('name', )
    empty_value_display = EMPTY_VALUE
    list_filter = ('name', )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug', )
    search_fields = ('name', )
    empty_value_display = EMPTY_VALUE
    list_filter = ('name', )


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe', 'id', )
    search_fields = ('user', )
    empty_value_display = EMPTY_VALUE
    list_filter = ('user', )


@admin.register(FavoriteRecipe)
class FavAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe', )
    search_fields = ('user', )
    empty_value_display = EMPTY_VALUE
    list_filter = ('user', )


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = (IngredientRecipeInline, TagRecipeInline)
    list_display = ('name', 'author', 'time', 'id', 'count_favs', 'pub_date', )
    search_fields = ('name', 'author', 'tag')
    empty_value_display = EMPTY_VALUE
    list_filter = ('name', 'author', 'tag')

    def count_favs(self, obj):
        return FavoriteRecipe.objects.filter(recipe=obj).count()


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('user', 'following', )
    search_fields = ('user', )
    empty_value_display = EMPTY_VALUE
    list_filter = ('user', )
