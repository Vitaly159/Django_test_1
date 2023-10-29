from django.db import models


class Todo(models.Model):
    is_complete = models.BooleanField('Завершено', default=False)
    user = models.CharField('Пользователь', max_length=50, default=None)

    class Meta():
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    # def __str__(self):
    #     return self.title
