from django.shortcuts import render

from .models import Date

def index(request):
    """The home page for Learning Log."""
    return render(request, 'daisy_diary_app/index.html')

def dates(request):
    """Show all topics."""
    dates = Date.objects.order_by('date_added')
    context = {'dates': dates}
    return render(request, 'daisy_diary_app/dates.html', context)

def date(request, date_id):
    """Show a single topic, and all its entries."""
    date = Date.objects.get(id=date_id)
    entries = date.entry_set.order_by('-date_added')
    context = {'date': date, 'entries': entries}
    return render(request, 'daisy_diary_app/date.html', context)
