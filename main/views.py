from django.shortcuts import render


def home(request):
    context = {'home' : 'active'}
    return render(request, 'home.html', context)


def services(request):
    context = {'services': 'active'}
    return render(request, 'services.html', context)


def skill(request):
    context = {'context' : 'active'}
    return render(request, 'skill.html', context)


def team(request):
    context = {'team' : 'active'}
    return render(request, 'team.html', context)


def portfolio(request):
    context = {'portfolio': 'active'}
    return render(request, 'portfolio.html', context)


def contact(request):
    context = {'contact' : 'active'}
    return render(request, 'contact.html', context)