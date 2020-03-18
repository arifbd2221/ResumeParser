from django.db import models
from django.utils import timezone

class Resume(models.Model):
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.created

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    experience = models.FloatField()
    total_skills = models.IntegerField()
    designation = models.CharField(max_length=50)
    company = models.CharField(max_length=100)

    def __str__(self):
        return self.email





class PersonInfo(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=20)
    phone = models.CharField(max_length=50)
    total_experience = models.FloatField()
    designation = models.CharField(max_length=50)
    skills = models.ForeignKey('Skill',on_delete=models.CASCADE)

class Skill(models.Model):
    person = models.ForeignKey('PersonInfo', on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=50)

