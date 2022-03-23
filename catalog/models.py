from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from catalog.validators import validate_catalog_text
from core.models import Base, BaseSlug


class Tag(BaseSlug):
    """
    Модель тэга для товаров
    """

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Category(BaseSlug):
    """
    Модель категории товара
    """

    weight = models.IntegerField(default=100,
                                 help_text='Максимум 32767',
                                 verbose_name='Вес',
                                 validators=[MaxValueValidator(32767),
                                             MinValueValidator(1)])

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Item(Base):
    """
    Модель товара
    """

    name = models.CharField(
        max_length=150, verbose_name='Название',
        help_text='Максимум 150 символов'
    )

    text = models.TextField(
        validators=[validate_catalog_text],
        verbose_name='Описание',
        help_text='Минимум 2 слова, используйте "роскошно/превосходно"'
    )

    category = models.ForeignKey(Category, on_delete=models.RESTRICT,
                                 default=None, verbose_name='Категория',
                                 help_text='Категория товара')

    tags = models.ManyToManyField(Tag, default=None, verbose_name='Тэги')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
