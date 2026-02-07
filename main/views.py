from django.shortcuts import render
from .models import Drug

def search_drug(request):
    query = request.GET.get('q')
    drug = None

    if query:
        try:
            drug = Drug.objects.get(name__icontains=query)
        except Drug.DoesNotExist:
            drug = None

    return render(request, 'search.html', {
        'drug': drug,
        'query': query
    })

