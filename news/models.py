from django.db import models

class News(models.Model):
    title = models.CharField(
        max_length = 50, verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    def str(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'новость'






# python manage.py makemigrations
# migrate