from django.db import models
from django.urls import reverse

class Student(models.Model):

    name=models.CharField(max_length=205)
    school = models.CharField(max_length=205)
    email=models.EmailField(blank=True)

    class Meta:
        verbose_name="Оқушы"
        verbose_name_plural = "Оқушылар"
        ordering=['name','school']

class Categories(models.Model):

    title=models.CharField(max_length=255)
    content = models.TextField(blank=True)
    describe=models.TextField(default='Dataflair Django tutorials')


class Posts(models.Model):
    title = models.CharField(max_length=255, verbose_name='Тақырып')
    is_published = models.BooleanField(default=True, verbose_name='Шығарылым')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def get_absolute_url(self):
        return reverse('post',kwargs={'post_slug': self.slug})

