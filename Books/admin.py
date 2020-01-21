# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import AllBooks , recentlyOpened , userFav , userUploads
from django.contrib import admin

# Register your models here.
admin.site.register(AllBooks)
admin.site.register(recentlyOpened)
admin.site.register(userFav)
admin.site.register(userUploads)