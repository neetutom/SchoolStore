from django.db import models
from django.urls import reverse


# Create your models here.
class Department(models.Model):
    dept_name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    dept_desc = models.TextField()
    dept_image = models.ImageField(upload_to='department', blank=True)

    class Meta:
        ordering = ('dept_name',)
        verbose_name = 'department'
        verbose_name_plural = 'departments'

    def __str__(self):
        return '{}'.format(self.dept_name)

    def get_url(self):
        return reverse('storeApp:details', args=[self.slug])


class Course(models.Model):
    course_name = models.CharField(max_length=250, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        ordering = ('course_name',)
        verbose_name = 'course'
        verbose_name_plural = 'courses'

    def __str__(self):
        return '{}'.format(self.course_name)

class Order(models.Model):
    gender_choices = (
        ('M','Male'),
        ('F', 'Female'),
    )
    name = models.CharField(max_length=250, blank=False)
    dob = models.DateField(null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=6, choices=gender_choices, blank=False)
    phone_number = models.CharField(max_length=15, blank=True)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=250, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)
    stationary = models.CharField(max_length=20)

    def __str__(self):
        return '{}'.format(self.name)


