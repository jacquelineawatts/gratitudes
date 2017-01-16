from django.contrib import admin
from .models import Entry, Comment, Gratitude

admin.site.register(Entry)
admin.site.register(Comment)
admin.site.register(Gratitude)
