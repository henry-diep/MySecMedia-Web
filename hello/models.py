from django.db import models

import datetime

# Create your models here.
class NewsItem(models.Model):

    title = models.CharField(
        unique=True, 
        null = False,
        blank = False,
        max_length=50
        )

    description = models.CharField(
        unique=True, 
        null = False,
        blank = False,
        max_length=200
        )

    link = models.CharField(
        unique=True, 
        null = False,
        blank = False,
        max_length=50
        )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("NewsItem_detail", kwargs={"pk": self.pk})


class Author(models.Model):

    name = models.CharField(
        null=False,
        max_length=50
        )
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

class Feedmodel(models.Model):
    title_name = models.CharField(max_length=140)
    url_link = models.CharField(unique=True, max_length=140)
    feed_site = models.CharField(max_length=140)
    load_datetime = models.DateTimeField(blank=True,null=True,default=datetime.date.today)
    publish_date = models.CharField(max_length=140)
    description = models.CharField(max_length=200, default='No value')
    feed_site_url = models.CharField(max_length=200, default='No value')

    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title_name