from django.http import HttpResponse

from django.shortcuts import render

data = {
    'journals': [
        {
            'id': 5,
            'fname': 'Dominik',
            'sname': 'Trochonowicz',
            'dob': '29-11-2022'
        },
        {
            'id': 6,
            'fname': 'Jan',
            'sname': 'Kochanowski',
            'dob': '15-02-1976'
        },
        {
            'id': 7,
            'fname': 'Grzegorz',
            'sname': 'Trochonowicz',
            'dob': '15-01-1971'
        }
        
        ]   
}

def journal(request):
    return render(request, 'journal/journal.html', data)

def home(request):
    return HttpResponse('Home page')