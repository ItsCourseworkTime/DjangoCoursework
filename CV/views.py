from django.shortcuts import render


def cvhome(request):
    return render(request, 'CV/cvhome.html')
    
def cvedit(request):
    return render(request, 'CV/cvedit.html')