from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.db.models import Avg, Max, Min

from .models import Widget

def index(request):
    try:
        widget = Widget.objects.all()
        return render(request, 'index.html', {'widget': widget})
    except:
        return render(request, 'index.html')


def create(request):
    Widget.objects.create(
        description=request.POST['description'],
        quantity=request.POST['quantity'],
    )
    return redirect('/')


def delete(request, w_id):
    widget = Widget.objects.get(id=w_id)
    widget.delete()
    return redirect('/')
