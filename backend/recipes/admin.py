from django.contrib import admin

from recipes.models import (Favorite, Ingredient, Recipe, RecipeIngredient,
                            Shopping, Tag)


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


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'user')


admin.site.register(Favorite, FavoriteAdmin)


class ShoppingAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'user')


admin.site.register(Shopping, ShoppingAdmin)
