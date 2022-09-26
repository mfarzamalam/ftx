from django.shortcuts import render

# Create your views here.

def index_view(request):
    context = {'active':'index'}
    return render(request, 'index.html', context)


def about_view(request):
    context = {'active':'about'}
    return render(request, 'about.html', context)


def services_view(request):
    context = {'active':'services'}
    return render(request, 'services.html', context)


def accounts_view(request):
    context = {'active':'accounts'}
    return render(request, 'accounts.html', context)


def contact_view(request):
    context = {'active':'contact'}
    return render(request, 'contact.html', context)