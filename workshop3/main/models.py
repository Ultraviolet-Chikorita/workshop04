from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name + " who is " + str(self.age) + " years old" 

class Pet(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    owner = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='pets')

    def __str__(self):
        return self.name + " owned by " + str(self.owner)

class SpiritAnimal(models.Model):
    name = models.CharField(max_length=100)
    power_level = models.IntegerField()
    owner = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='spirit_animal')

    def __str__(self):
        return self.name + " with power level " + str(self.power_level) + " owned by " + str(self.owner)
    
class PlacesVisited(models.Model):
    person = models.ManyToManyField(Person, related_name='places_visited')
    place_name = models.CharField(max_length=200)

    def __str__(self):
        return self.place_name + " visited by " + "; ".join([str(person) for person in self.person.all()])
    
class BirthCertificate(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='birth_certificate')
    certificate_number = models.CharField(max_length=100)
    issue_date = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
        return "Birth Certificate " + self.certificate_number + " for " + str(self.person)