from django.db import models
from django.utils import timezone

class Entry(models.Model):

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return '{}: {}'.format(self.author, self.text)


class Comment(models.Model):

    author = models.ForeignKey('auth.User')
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)


class Gratitude(models.Model):

    author = models.ForeignKey('auth.User')
    text = models.TextField()
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
