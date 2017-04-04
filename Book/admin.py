from django.contrib import admin

# Register your models here.

from .models import Author, Publisher, Book

admin.site.register([Author, Publisher, Book])