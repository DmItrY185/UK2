from django.shortcuts import render
from main.models import Code


def index(request):
    query = request.POST.get('q', None)

    if query:
        value = Code.objects.filter(code=query)

        if value.exists():
            query = 'Yes'

    context = {
        'code': query
    }

    return render(request, 'main/index.html', context=context)


def pageNotFound(request, exception):
    return render(request, 'main/error.html')
