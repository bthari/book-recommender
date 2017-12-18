import sys
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import QueryForms

response = {}
data = {"books": [{"id": "1", "title": "A", "desc": "AAAA"},
                  {"id": "1", "title": "A", "desc": "AAAA"},
                  {"id": "1", "title": "A", "desc": "AAAA"}]}


def results(request):
    return render(
        request,
        'results.html',
    )


def search_books(request):
    form = QueryForms(request.GET or None)

    if request.method == 'GET' and form.is_valid():
        response["query"] = request.GET['query_book']
        print(response["query"])

        return HttpResponseRedirect("/retrieve/results/", {'data': data})

    else:
        form = QueryForms()

    return render(request, 'index.html', {'form': form})

