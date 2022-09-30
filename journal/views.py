from django.http import HttpResponse

from django.shortcuts import render
def journal(request):
    return render(request, 'journal/journal.html')

def home(request):
    return HttpResponse('Home page')