from django.shortcuts import render


def cvhome(request):
    return render(request, 'CV/cvhome.html')