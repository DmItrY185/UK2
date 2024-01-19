from django.shortcuts import render
from main.models import Code


def index(request):
    query = request.GET.get('q', None)

    # if query:
    #     value = Code.objects.filter(code=query)
    #
    #     if value.exists():
    #         query = 'Yes'
    #
    # context = {
    #     'code': query
    # }

    name = ''
    if query:
        value = Code.objects.filter(code=query)

        if value.exists():
            query = 'Yes'
            name = value[0].name

    context = {
        'code': query,
        'name': name
    }

    return render(request, 'main/index.html', context=context)


def pageNotFound(request, exception):
    return render(request, 'main/error.html')
