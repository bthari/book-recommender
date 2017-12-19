import sys
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import QueryForms
from .similarities import find_similar_title, find_similar_desc

response = {}

# data = {"books":[{"title": "HEHEHE", "desc": "HEHEHHEHEE"}, 
# {"title": "HEHEHE", "desc": "HEHEHHEHEE"},
# {"title": "HEHEHE", "desc": "HEHEHHEHEE"}]}

def index(request):
    return render(request, "results.html", response)


def results(request):
    return render(
        request,
        'results.html',
    )


def search_by_title(request):
    form = QueryForms(request.GET or None)

    if request.method == 'GET' and form.is_valid():
        response["query"] = request.GET['query_book']
        print(request.GET['query_book'] + "end")
        data = find_similar_title(request.GET['query_book'])
        print(data)
        print(response["query"])

        return render(request, 'results.html', {'data': data})

    else:
        form = QueryForms()

    return render(request, 'index.html', {'form': form})


def search_by_desc(request):
    form = QueryForms(request.GET or None)

    if request.method == 'GET' and form.is_valid():
        response["query"] = request.GET['query_book']
        print(request.GET['query_book'] + "end")
        data = find_similar_desc(request.GET['query_book'])
        print(data)
        print(response["query"])

        return render(request, 'results.html', {'data': data})

    else:
        form = QueryForms()

    return render(request, 'index.html', {'form': form})