from django.core.exceptions import ValidationError
from django.db import models

from cities.models import City


class Route(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название маршрута')
    travel_times = models.PositiveSmallIntegerField(verbose_name='Общее время в пути')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='route_from_city_set',
                                  verbose_name='Откуда')
    to_city = models.ForeignKey('cities.City', on_delete=models.CASCADE, related_name='route_to_city_set',
                                verbose_name='Куда')
    trains = models.ManyToManyField('trains.Train', verbose_name='Список поездов')

    def __str__(self):
        return f'Маршрут {self.name} из {self.from_city}'

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'
        ordering = ['travel_times']

    # def clean(self):
    #     if self.from_city == self.to_city:
    #         raise ValidationError('Измените город прибытия/отправления')
    #     qs = Route.objects.filter(travel_time=self.travel_times,
    #                               from_city=self.from_city,
    #                               to_city=self.to_city).exclude(pk=self.pk)
    #     # Train == self.__class__
    #     if qs.exists():
    #         raise ValidationError('Измените время в пути')
    #
    # def save(self, *args, **kwargs):
    #     self.clean()
    #     super().save(*args, **kwargs)
