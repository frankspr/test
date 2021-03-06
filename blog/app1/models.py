#cofing:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.urls import reverse
@python_2_unicode_compatible
class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
    	return self.name

@python_2_unicode_compatible
class Tag(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
    	return self.name

@python_2_unicode_compatible
class Post(models.Model):

    title = models.CharField(max_length=70)

    body = models.TextField()

    
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()


    excerpt = models.CharField(max_length=200, blank=True)


    # https://docs.djangoproject.com/en/1.10/topics/db/models/#relationships
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    author = models.ForeignKey(User)

    def __str__(self):
    	return self.title


    def get_absolute_url(self):
        return reverse('app1:detail', kwargs={'pk': self.pk})
