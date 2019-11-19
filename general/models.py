from django.contrib.auth.models import User
from django.db import models


class Place(models.Model):
    PLACE_FEATURES = (
        (1, 'Оплата по карте'),
        (2, 'Алкоголь'),
        (3, 'Туалет'),
        (4, 'Гигиена на кухне'),
        (5, 'Вегетарианская кухня')
    )

    latitude = models.CharField(
        max_length=10,
        null=False,
        blank=True,
        verbose_name='Широта'
    )
    longitude = models.CharField(
        max_length=10,
        null=False,
        blank=True,
        verbose_name='Долгота'
    )
    title = models.CharField(
        max_length=50,
        null=False,
        blank=True,
        verbose_name='Название'
    )
    rating = models.FloatField(
        default=0,
        null=True,
        blank=True,
        verbose_name='Рейтинг'
    )
    address = models.CharField(
        max_length=300,
        null=False,
        blank=True,
        verbose_name='Адрес'
    )
    open_hours = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name='Часы работы'
    )
    average_check = models.FloatField(
        null=True,
        blank=True,
        verbose_name='Средний чек'
    )
    views = models.IntegerField(
        default=0,
        blank=True,
        verbose_name='Количество просмотров'
    )
    feature = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Особенность',
        choices=PLACE_FEATURES
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заведение'
        verbose_name_plural = 'Заведения'


class Report(models.Model):
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
        verbose_name='Автор'
    )
    review = models.CharField(
        max_length=3000,
        null=False,
        blank=True,
        verbose_name='Рецензия'
    )
    date = models.DateTimeField(
        blank=True,
        verbose_name='Дата публкации'
    )
    mark = models.IntegerField(
        blank=True,
        null=False,
        verbose_name='Оценка'
    )

    def __str__(self):
        return self.author.first_name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Rate(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Заведение'
    )
    mark = models.IntegerField(
        null=False,
        blank=True,
        verbose_name='Пользовательская оценка'
    )

    def __str__(self):
        return self.place.title

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'
