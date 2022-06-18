from colorfield.fields import ColorField
from django.core.validators import MinValueValidator
from django.db import models
from users.models import User


class Ingredient(models.Model):
    name = models.CharField(
        'Наименование',
        max_length=155,
        help_text='Наименование ингредиента'
    )
    unit = models.CharField(
        'Наименование',
        max_length=50,
        help_text='Единица измерения'
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self) -> str:
        return self.name


class Tag(models.Model):
    name = models.CharField(
        'Тег',
        max_length=200,
        help_text='Имя тега'
    )
    color = ColorField(
        format='hex',
        verbose_name='Цвет',
        help_text='Выберите цвет тега'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Уникальный идентификатор',
        help_text='Введите уникальный идентификатор'
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self) -> str:
        return self.slug


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор',
    )
    name = models.CharField(
        'Название блюда',
        max_length=200,
        help_text='Как называется Ваше блюдо?'
    )
    image = models.ImageField(
        'Фото',
        upload_to='recipes/images/',
        help_text='Как выглядит ваше блюдо?'
    )
    text = models.TextField(
        'Текст рецепта',
        help_text='Как будем готовить?'
    )
    time = models.IntegerField(
        validators=[
            MinValueValidator(
                1,
                'Минимальное время приготовления - 1')],
        verbose_name='Время приготовления',
        help_text='Сколько времени будем готовить?')
    ingredients = models.ManyToManyField(
        Ingredient,
        through='IngredientRecipe',
        related_name='recipes',
        verbose_name='Ингредиенты для блюда',
        help_text='Что нужно для приготовления?'
    )
    tag = models.ManyToManyField(
        Tag,
        through='TagRecipe',
        verbose_name='Тег',
        help_text='Укажите теги вашего блюда'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='carts',
        verbose_name='Рецепты'
    )

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'recipe',),
                name='unique_cart'
            ),
        )

    def __str__(self):
        return f'У пользователя {self.user} в корзине {self.recipe}'


class Subscribe(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='followed'
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = (
            models.UniqueConstraint(fields=('user', 'following',),
                                    name='unique_subscribe'),
        )

    def __str__(self):
        return f'Пользователь {self.user} подписан на {self.followed}'


class IngredientRecipe(models.Model):
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='ingredientsrecipe',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredientsrecipe',
    )
    amount = models.PositiveSmallIntegerField(
        default=1,
    )

    class Meta:
        verbose_name = 'Игредиенты рецепта'
        constraints = (
            models.UniqueConstraint(fields=('ingredient', 'recipe',),
                                    name='unique_ingredientrecipe'),
        )

    def __str__(self):
        return f'{self.ingredient} {self.recipe}'


class TagRecipe(models.Model):
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        verbose_name='Теги'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт'
    )

    class Meta:
        verbose_name = 'Теги рецепта'
        constraints = (
            models.UniqueConstraint(fields=('tag', 'recipe',),
                                    name='unique_tagrecipe'),
        )

    def __str__(self):
        return f'{self.tag} {self.recipe}'


class FavoriteRecipe(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Юзер'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorites'
    )

    class Meta:
        verbose_name = 'Избранный'
        verbose_name_plural = 'Избранные'
        constraints = (
            models.UniqueConstraint(fields=('user', 'recipe',),
                                    name='unique_favorite'),
        )

    def __str__(self):
        return f'{self.recipe} {self.user}'
