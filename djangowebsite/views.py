from django.shortcuts import render, redirect
from datetime import datetime
from .forms import NewsletterForm
from .models import UserWebsite


def introduction(request):
    return render(request, 'introduction.html', {'current_date_time': datetime.now})


def presentation(request):
    return render(request, 'presentation.html', {'current_date_time': datetime.now})


def covidreport(request):
    return render(request, 'covidreport.html', {'current_date_time': datetime.now})


def newsletter(request):
    if len(request.POST) > 0:
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/userinfo')
        else:
            return render(request, 'newsletter.html', {'form': form})
    else:
        form = NewsletterForm()

    return render(request, 'newsletter.html', {'current_date_time': datetime.now, 'form': form})


def userinfo(request):
    all_users = UserWebsite.objects.all()
    return render(request, 'userinfo.html', {'current_date_time': datetime.now, 'all_users': all_users})
