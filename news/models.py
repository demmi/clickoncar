from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

import os


class Author(models.Model):
    name = models.CharField(blank=False, max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100, blank=False)
    url = models.SlugField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    tags = models.CharField(max_length=100, blank=False)
    text = RichTextUploadingField(blank=False)
    datetime = models.DateTimeField(auto_now_add=True)
    datetime_modify = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
