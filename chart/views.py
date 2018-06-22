from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect
from .models import chart_row
from .forms import chart_row_add
from .plot import chart_make

def chart_rows(request):
    crows = chart_row.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'chart/chart_rows.html', {'crows':crows})

def crow_add(request):
    if request.method == "POST":
        form = chart_row_add(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            chart_make.apply_async((post.id, ), countdown = 3, expires= 15)
            
            return redirect('/')
    else:
        form = chart_row_add()
    return render(request, 'chart/crow_add.html', {'form': form})
