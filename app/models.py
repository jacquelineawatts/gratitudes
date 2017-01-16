from django.db import models
from django.utils import timezone


class Entry(models.Model):

    created_date = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=False)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return '{}'.format(self.created_date)


class Gratitude(models.Model):

    author = models.ForeignKey('auth.User')
    text = models.TextField()
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)

    def __str__(self):
        return 'Post by {}:{}'.format(self.author, self.text)


class Comment(models.Model):

    author = models.ForeignKey('auth.User')
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    gratitude = models.ForeignKey(Gratitude, on_delete=models.CASCADE)

    def __str__(self):
        return 'Comment by {}: {}'.format(self.author, self.text)
