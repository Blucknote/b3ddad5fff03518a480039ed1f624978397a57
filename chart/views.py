from django.shortcuts import render
from django.utils import timezone
from .models import chart_row

def chart_rows(request):
    crows = chart_row.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'chart/chart_rows.html', {'crows':crows})
# Create your views here.
