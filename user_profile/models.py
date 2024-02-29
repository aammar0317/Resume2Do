from django.db import models
#from django.utils import timezone
#from django.contrib.auth.models import User
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    profile_image = models.ImageField(null=True, blank=True)
    address = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=14)
    email=models.EmailField(max_length=100)
    linkedin = models.CharField(max_length=100)
    summary = models.TextField(max_length=1000)
    skill1 = models.CharField(max_length=100)
    skill2 = models.CharField(max_length=100)
    skill3 = models.CharField(max_length=100)
    skill4 = models.CharField(max_length=100)
    skill5 = models.CharField(max_length=100)
    skill6 = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    from_date = models.DateField()
    to_date = models.DateField()
    company_name = models.CharField(max_length=100)
    country = models.CharField(max_length=300)
    job_role1 = models.TextField(max_length=500)
    job_role2 = models.TextField(max_length=500)
    job_role3 = models.TextField(max_length=500)
    job_role4 = models.TextField(max_length=500)
    job_role5 = models.TextField(max_length=500)
    language1 = models.CharField(max_length=100)
    language2 = models.CharField(max_length=100)
    language3 = models.CharField(max_length=100)
    hobbies1 = models.CharField(max_length=100)
    hobbies2 = models.CharField(max_length=100)
    hobbies3 = models.CharField(max_length=100)
    hobbies4 = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    institute_name = models.CharField(max_length=100)
    passing_year = models.CharField(max_length=100)
    country_name = models.CharField(max_length=100)
    certificate_name1 = models.CharField(max_length=100)
    course1 = models.CharField(max_length=100)
    certificate_name2 = models.CharField(max_length=100)
    course2 = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name




    

