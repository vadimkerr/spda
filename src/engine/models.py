# Фамилия
# Имя
# Название курса
# Ссылка на курс
# Цена курса(опционально)
# Дата начала курса(опционально)
# Квартал обучения(списочное)
# Обоснование(текстовое)
from django.contrib.auth.models import User
from django.db import models


class Application(models.Model):
    class Quarter(models.IntegerChoices):
        Q1 = 1, "Q1"
        Q2 = 2, "Q2"
        Q3 = 3, "Q3"
        Q4 = 4, "Q4"

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="applications"
    )
    title = models.CharField(max_length=200)
    link = models.URLField()
    price = models.CharField(max_length=50, null=True, default=None)
    start_date = models.DateField(null=True, default=None)
    quarter = models.PositiveSmallIntegerField(choices=Quarter.choices)
    justification = models.TextField()
