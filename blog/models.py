from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class News(models.Model):
    title = models.CharField('Name post', max_length=100, unique=True)
    content = models.TextField('Content')
    text = models.TextField('Main text post')
    date = models.DateTimeField('Date publication', default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.IntegerField('views',default=1)
    # sizes = (
    # ('S', 'Small'),
    # ('M', 'Medium'),
    # ('L', 'Large'),
    # )
    # shop_sizes = models.CharField(choices=sizes, max_length=1, default='S')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def get_absolute_url(self):
        return reverse ('news-detail', kwargs={'pk':self.pk})

from django.db import models

class ContactMessage(models.Model):
    subject = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject