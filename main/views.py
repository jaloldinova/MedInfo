from django.shortcuts import render
from .models import Drug

def search_drug(request):
    query = request.GET.get('q')
    drugs = Drug.objects.filter(name__icontains=query) if query else []

    return render(request, 'search.html', {
        'drugs': drugs,
        'query': query
    })
