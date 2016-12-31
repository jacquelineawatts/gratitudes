from django.shortcuts import render
from .models import Entry
from django.utils import timezone

def entries(request):
    entries = Entry.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'app/entries.html', {'entries': entries})
