from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, 'index.html')


# def studentRegister(request):
#     return render(request, 'student-register.html')

# company register interface


def comRegister(request):
    if request.method == 'POST':
        comName = request.POST['comName']
        comEmail = request.POST['comEmail']
        compassword = request.POST['comPassword']
        cPassword = request.POST['comePasswordconfirm']
        role = request.POST['role']

        if compassword == cPassword:
            if User.objects.filter(email=comEmail).exists():
                messages.info(request, 'Email Already in used')
                return redirect('comRegister')
            else:
                user = User.objects.create(
                    username=comEmail, email=comEmail, first_name=comName, last_name=role)
                user.set_password(compassword)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not matching please enter again')
            return redirect('comRegister')
    else:
        return render(request, 'com-register.html')


# Student register interface
def studentRegister(request):
    if request.method == 'POST':
        studentName = request.POST['studentName']
        studentEmail = request.POST['studentEmail']
        userpassword = request.POST['studentPassword']
        cPassword = request.POST['studentPasswordconfirm']
        role = request.POST['role']

        if userpassword == cPassword:
            if User.objects.filter(email=studentEmail).exists():
                messages.info(request, 'Email Already in used')
                return redirect('studentRegister')
            else:
                user = User.objects.create(
                    username=studentEmail, email=studentEmail, first_name=studentName, last_name=role)
                user.set_password(userpassword)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not matching please enter again')
            return redirect('studentRegister')
    else:
        return render(request, 'student-register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        # role = request.POST['type']

        user = authenticate(
            request, username=email, password=password)

        if user is not None:
            auth_login(request, user)
            if user.last_name == "student":
                # return render(request, 'home-student.html')
                return redirect('homeStudent')
            elif user.last_name == "company":
                # return render(request, 'home-company.html')
                return redirect('company_portal')
        else:
            messages.info(request, "Credential Invalid")
            return redirect('login')

    else:
        return render(request, 'login.html')


def homeStudent(request):
    return render(request, 'home-student.html')


@login_required(login_url='login')
def homeCompany(request):
    if request.method == 'POST':
        title = request.POST['ititle']
        address = request.POST['address']
        description = request.POST['idescription']
        name = request.POST['cname']
        email = request.POST['email']
        tPhone = request.POST['tpno']

        post = Post.objects.create(internTitle=title, companyAddress=address,
                                   internshipDescription=description, comName=name, email=email, tPhone=tPhone)
        post.save()
        return redirect('company_portal')

    else:
        return render(request, 'home-company.html')


@login_required(login_url='login')
def homeStudent(request):
    return render(request, 'home-student.html')


@login_required(login_url='login')
def company_portal(request):
    posts = Post.objects.all()
    return render(request, 'company-portal.html', {'jobposts': posts})


@login_required(login_url='login')
def search_result(request):
    if request.method == 'POST':
        searchKeyword = request.POST['search']
        posts = Post.objects.all()
        if posts is not None:
            result = posts.filter(internTitle__icontains=searchKeyword)
            return render(request, 'search-result.html', {'searchResults': result})


def log_out(request):
    logout(request)
    return redirect('login')


def remove(request):
    id = request.POST['id']
    Post.objects.filter(id=id).delete()
    return redirect('company_portal')
