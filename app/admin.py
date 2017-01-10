from django.contrib import admin
from .models import Entry, Comment, Gratitude

admin.site.register(Entry)
admin.site.register(Gratitude)
admin.site.register(Comment)
