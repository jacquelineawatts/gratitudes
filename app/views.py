from django.shortcuts import render, redirect
from .models import Entry
from .forms import EntryForm
from django.utils import timezone


def entries(request):
    entries = Entry.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    form = EntryForm()
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            return redirect('entries')

    return render(request, 'app/entries.html', {'entries': entries, 'form': form})
