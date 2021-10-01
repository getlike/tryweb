from django.db import models

# Create your models here.
class Rubric(models.Model):
    name = models.CharField(max_length=20,db_index=True, verbose_name='название')
    def __str__(self):
        return self.name
    class Meeta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрик'
        ordering = ['name']

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True,blank=True, verbose_name='цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')

    #зависимость на внешний ключ

    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика') #54 page

    class Meta:
        verbose_name_plural = 'Обьявления'
        verbose_name = 'Обьявление'
        ordering = ['-published']
