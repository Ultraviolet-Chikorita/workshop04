from django.shortcuts import render
from .models import Person

# Create your views here.

def home(request):
    return render(request, 'home.html')

def home2(request, name):
    people = Person.objects.filter(name=name)
    if people.exists():
        person = str(people.first())
    else:
        person = "Unidentified Person"
    return render(request, 'home2.html', {'name': person})

def makeperson(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        person = Person(name=name, age=age)
        person.save()
        return render(request, 'makeperson.html', {'message': 'Person created successfully!'})
    return render(request, 'makeperson.html', {'message': ''})

def getLegalPeople(request):
    people = Person.objects.filter(age__gte=18)
    return render(request, 'legalpeople.html', {'people': people})

def getPetsOfPerson(request, name):
    people = Person.objects.filter(name=name)
    if people.exists():
        person = people.first()
        pets = person.pets.all()
        return render(request, 'pets.html', {'pets': pets})
    else:
        return render(request, 'pets.html', {'pets': []})