from django.shortcuts import render, redirect
from .models import CVSection


def getCVContext():
    sections = CVSection.objects.all()
    
    pstatement = sections.filter(title = 'pstatement').first()
    education = sections.filter(title = 'education').first()
    achievments = sections.filter(title = 'achievments').first()
    wexperience = sections.filter(title = 'wexperience').first()
    
    context = {
        'pstatement': pstatement,
        'education': education,
        'achievments': achievments,
        'wexperience': wexperience
    }
    
    return context

def cvhome(request):
    return render(request, 'CV/cvhome.html', getCVContext())
    
def cvedit(request):
    if request.method == 'POST':
        sections = CVSection.objects.all()
        
        pstatement = sections.filter(title = 'pstatement').first()
        education = sections.filter(title = 'education').first()
        achievments = sections.filter(title = 'achievments').first()
        wexperience = sections.filter(title = 'wexperience').first()
        
        #Populate database if these sections do not yet exist
        if pstatement == None:
            pstatement = CVSection(title = 'pstatement')
        if education == None:
            education = CVSection(title = 'education')
        if achievments == None:
            achievments = CVSection(title = 'achievments')
        if wexperience == None:
            wexperience = CVSection(title = 'wexperience')
        
        #Update entries and save
        pstatement.text = request.POST['pstatement']
        education.text = request.POST['education']
        achievments.text = request.POST['achievments']
        wexperience.text = request.POST['wexperience']
        
        pstatement.save()
        education.save()
        achievments.save()
        wexperience.save()

        return redirect('/CV/')
    return render(request, 'CV/cvedit.html', getCVContext())