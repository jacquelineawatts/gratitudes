from django.shortcuts import render, redirect
from .models import Entry
from .forms import EntryForm, GratitudeForm
from django.utils import timezone


def entries(request):
    entries = Entry.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')

    grat_form = GratitudeForm()
    entry_form = EntryForm()
    if request.method == "POST":
        grat_form = GratitudeForm(request.POST)
        if grat_form.is_valid():
            gratitude = grat_form.save(commit=False)
            gratitude.author = request.user
            gratitude.save()
            entry = entry_form.save(commit=False)
            entry.created_date = timezone.now()
            entry.save()

            return redirect('entries')

    return render(request, 'app/entries.html', {'entries': entries, 'form': grat_form})


def profiles(request):
    profile = User.objects.get()

    return render(request, 'app/profile.html', {'user': user, 'form': profile_form})