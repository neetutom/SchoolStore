from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from storeApp.forms import OrderCreationForm
from storeApp.models import Course, Order


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('register:createorder'))
        else:
            messages.info(request, "Please enter valid credentials")
            return HttpResponseRedirect (reverse ('register:login'))
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists.")
                return HttpResponseRedirect (reverse ('register:register'))
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                messages.info(request, "User created successfully")
                return HttpResponseRedirect (reverse ('register:login'))
        else:
            messages.info(request, "Passwords do not match")
            return HttpResponseRedirect (reverse ('register:register'))

    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def CreateOrder(request):
    form=OrderCreationForm()
    if request.method == 'POST':
        form = OrderCreationForm(request.POST)
        print(form.data)
        if form.is_valid():
            form.save()
            messages.info(request, "Order Submitted Successfully")
            return render(request, "message.html")
        else:
            messages.info(request, "There was an error in saving the form")
            return HttpResponseRedirect(reverse('register:createorder'))
    return render(request, 'formPage.html', {'form': form})

# AJAX
def load_courses(request):
    # print("I have reached load_courses function ")
    department_id = request.GET.get('department_id')
    # print(department_id)
    courses = Course.objects.filter(department_id=department_id)
    # print(list(courses.values('id', 'course_name')))
    # return render(request, 'course_dropdown_list_options.html', {'courses': courses})
    return JsonResponse(list(courses.values('id', 'course_name')), safe=False)