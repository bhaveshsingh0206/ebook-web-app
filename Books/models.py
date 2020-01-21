# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class AllBooks(models.Model):
    bookName = models.CharField(max_length=250)
    authorName = models.CharField(max_length=250)
    synopsis = models.CharField(max_length=10000)
    genre = models.CharField(max_length=250)
    authorName = models.CharField(max_length=250)
    ratings = models.CharField(max_length=10)
    trendingNow = models.BooleanField(default=False)
    date = models.CharField(max_length=20)
    thumbnailImage = models.FileField()
    bookCoverImage = models.FileField()
    review1 = models.CharField(max_length=400 , default="")
    review2 = models.CharField(max_length=400,default="")
    review3 = models.CharField(max_length=400,default="")
    bookPages = models.CharField(max_length=10,default="")
    secondName = models.CharField(max_length=100,default="")
    bookPDF = models.FileField()
    def __str__(self):
        return self.bookName + ' - ' + self.authorName

class recentlyOpened(models.Model):
    bookName = models.CharField(max_length=300)
    userName = models.CharField(max_length=200)
    def __str__(self):
        return self.userName + ' - ' + self.bookName

class userFav(models.Model):
        bookName = models.CharField(max_length=300)
        userName = models.CharField(max_length=200)
        def __str__(self):
            return self.userName + ' - ' + self.bookName

class userUploads(models.Model):
        bookName = models.CharField(max_length=300)
        userName = models.CharField(max_length=200)

        def __str__(self):
            return self.userName + ' - ' + self.bookName