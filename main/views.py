from django.shortcuts import render, redirect
from main.forms import ContactForm
from django.utils import timezone


def home(request):
    context = {'home': 'active'}
    return render(request, 'home.html', context)


def services(request):
    context = {'services': 'active'}
    return render(request, 'services.html', context)


def skill(request):
    context = {'context': 'active'}
    return render(request, 'skill.html', context)


def team(request):
    context = {'team': 'active'}
    return render(request, 'team.html', context)


def portfolio(request):
    context = {'portfolio': 'active'}
    return render(request, 'portfolio.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.message_date = timezone.now()
            form.save()
            return redirect('contactsuccess')
    else:
        form = ContactForm()

    context = {
        'form': form,
    }

    return render(request, 'contact.html', context)


def ContactSuccess(request):
    return render(request, 'contactsuccess.html', )
