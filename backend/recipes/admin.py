from django.contrib import admin

from recipes.models import (FavoriteList, Ingredient, Recipe, RecipeIngredient,
                            ShoppingList, Tag)


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    search_fields = ('name',)


admin.site.register(Ingredient, IngredientAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug')


admin.site.register(Tag, TagAdmin)


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'author')
    list_filter = ('name', 'author', 'tags')
    readonly_fields = ['favorite']

    def favorite(self, obj):
        return obj.favorite.count()
    favorite.short_description = 'Добавлено в избранное'


admin.site.register(Recipe, RecipeAdmin)


class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'amount')


admin.site.register(RecipeIngredient, RecipeIngredientAdmin)


class FavoriteListAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'user')


admin.site.register(FavoriteList, FavoriteListAdmin)


class ShoppingListAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'user')


admin.site.register(ShoppingList, ShoppingListAdmin)
