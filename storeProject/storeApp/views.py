from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import OrderCreationForm
from .models import Department, Course
from tkinter import *


# Create your views here.
def Home(request, d_slug=None):
    # print("I have reached Home View")
    departments = Department.objects.all
    return render(request, 'index.html')


def department_detail(request, c_slug):
    # print("I have reached details view")
    try:
        department = Department.objects.get(slug=c_slug)
        courses = Course.objects.all()
    except Exception as e:
        print("e: ", e)
        raise e
    return render(request, "department_detail.html", {'department': department, 'courses':courses})

