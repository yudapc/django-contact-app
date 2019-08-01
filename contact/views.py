from django.shortcuts import render, get_object_or_404, redirect
from .models import Person


def contact_list(request):
    persons = Person.objects.all().order_by('first_name')
    return render(request, 'contact/contact_list.html', {'persons': persons})