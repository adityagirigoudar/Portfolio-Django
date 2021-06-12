from django.shortcuts import render, HttpResponse

# Create your views here.
def Home(request):
    return render(request, 'home.html')
def AboutMe(request):
    return render(request, 'aboutme.html')
def PersonalProjects(request):
    return render(request, 'personalprojects.html')
def CollegeProjects(request):
    return render(request, 'collegeprojects.html')
def Achievements(request):
    return render(request, 'achievements.html')
def Contact(request):
    return render(request, 'contact.html')