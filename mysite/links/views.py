from django.shortcuts import render
from .models import Link
# Create your views here.


def my_view(request):
    link = Link.objects.all()

    return render(
        request,
        'my_template.html',
        {'links': link})
