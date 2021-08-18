from django.shortcuts import render

def all_forms(request):
    return render(request, 'forms/all_forms.html', {})