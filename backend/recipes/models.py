from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import UniqueConstraint

User = get_user_model()


class Ingredient(models.Model):
    """Ингредиент."""
    name = models.CharField(
        verbose_name='Название',
        max_length=50
    )
    measurement_unit = models.CharField(
        verbose_name='Единица измерения',
        max_length=15
    )

    class Meta:
        verbose_name = 'Ингредиент'

    def __str__(self):
        return f'{self.name}, {self.measurement_unit}'


class Tag(models.Model):
    """Тег."""
    name = models.CharField(
        verbose_name='Тэг',
        max_length=15,
        unique=True
    )
    color = models.CharField(
        verbose_name='Цвет',
        max_length=15,
    )
    slug = models.SlugField(
        max_length=15,
        unique=True
    )

    class Meta:
        verbose_name = 'Тег'

    def __str__(self):
        return f'{self.name}'


class Recipe(models.Model):
    """Рецепт."""
    author = models.ForeignKey(
        User,
        related_name='recipes',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Автор'
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=50
    )
    image = models.ImageField(
        upload_to='recipes',
        verbose_name='Изображение'
    )
    text = models.TextField(
        verbose_name='Описание'
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient',
        verbose_name='Ингредиенты',
        related_name='recipe'
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Теги',
        related_name='recipes'
    )
    cooking_time = models.PositiveSmallIntegerField(
        verbose_name='Время приготовления',
        validators=(MinValueValidator(
            limit_value=1,
            message='Время приготовления не может быть менее одной минуты.'),
        )
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Рецепт'

    def __str__(self):
        return f'{self.name}'


class RecipeIngredient(models.Model):
    """Количество ингредиента в рецепте."""
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
        related_name='recipe_ingredient'
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name='Ингредиент',
        related_name='recipe_ingredient'
    )
    amount = models.PositiveSmallIntegerField(
        verbose_name='Количество',
        validators=(MinValueValidator(
            limit_value=0.01,
            message='Количество не может быть меньше нуля'),
        )
    )

    class Meta:
        verbose_name = 'Количество ингредиента'
        constraints = [
            UniqueConstraint(
                fields=('recipe', 'ingredient'),
                name='ingredient must be inique for recipe'
            )
        ]

    def __str__(self):
        return (f'{self.recipe}: {self.ingredient.name},'
                f' {self.amount} {self.ingredient.measurement_unit}')


class Follow(models.Model):
    """Подписка."""
    user = models.ForeignKey(
        User,
        related_name='follower',
        verbose_name='Подписчик',
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User,
        related_name='following',
        verbose_name='Автор',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Подписка'
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'user'],
                name='unique_follower')
        ]

    def __str__(self):
        return f'Автор: {self.author}, подписчик: {self.user}'


class Favorite(models.Model):
    """Список избранного."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='favorite_list'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
        related_name='favorite_list'
    )

    class Meta:
        verbose_name = 'Список избранного'
        constraints = (
            UniqueConstraint(
                fields=('user', 'recipe'),
                name='unique favorite recipe'
            ),
        )

    def __str__(self):
        return f'{self.recipe} - {self.user}'


class Shopping(models.Model):
    """Список покупок."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='shopping_list'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
        related_name='shopping_list'
    )

    class Meta:
        verbose_name = 'Список покупок'
        constraints = (
            UniqueConstraint(
                fields=('user', 'recipe'),
                name='unique recipe for shopping list'
            ),
        )

    def __str__(self):
        return f'{self.recipe} - {self.user}'
