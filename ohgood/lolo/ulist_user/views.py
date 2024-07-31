from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Skill, Message
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm, ProfileForm, SkillForm, MessageForm# Assuming RegisterForm is defined in forms.py
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .utils import search_profile, paginateprofiles

def profile_list(request):
    profiles, search_query = search_profile(request)
    profiles, paginator = paginateprofiles(request,profiles)
    context = {'profiles': profiles, 'search_query': search_query, 'paginator': paginator}
    return render(request, 'ulist_user/profiles.html', context)

def profile_detail(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    projects = profile.project_set.all()
    skills = profile.skills.filter(description__isnull=False).all()
    return render(request, 'ulist_user/user-profile.html', {'profile': profile, 'projects': projects, 'skills': skills})

def custom_login(request):
    if request.user.is_authenticated:
        return redirect('profiles')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(request.GET['next'] if 'next'in request.GET else 'user_account')
            else:
                messages.error(request, 'Username or password is incorrect')
        else:
            messages.error(request, 'Invalid username or password')
    
    form = AuthenticationForm()
    return render(request, 'ulist_user/login_register.html', {'form': form, 'page': 'login'})

def custom_logout(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user
            messages.success(request, 'Account created successfully')
            return redirect('edit_account')
        else:
            messages.error(request, 'There was an error with your registration')
    else:
        form = RegisterForm()
    return render(request, 'ulist_user/login_register.html', {'form': form, 'page': 'register'})

@login_required(login_url='login')
def user_account(request):
    profile=request.user.profile
    projects = profile.project_set.all()
    context={'profile': profile, 'projects': projects}
    return render(request, 'ulist_user/user-account.html', context)


@login_required(login_url='login')
def edit_account(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account updated successfully')
            return redirect('user_account')
        else:
            messages.error(request, 'There was an error with your profile update')
    context = {'form': form}
    return render(request, 'ulist_user/profile_form.html', context)

@login_required(login_url='login')
def create_skill(request):
    user = request.user
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = Profile.objects.get(user=user)
            skill.save()
            messages.success(request, 'Skill created successfully')
            return redirect('user_account')

    context = {'form': form}
    return render(request, 'ulist_user/skill_form.html', context)

@login_required(login_url='login')
def update_skill(request, pk):
    print(f"Update Skill View called for skill id: {pk}")
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill updated successfully')
            return redirect('user_account')
    else:
        form = SkillForm(instance=skill)
    
    context = {'form': form}
    return render(request, 'ulist_user/skill_form.html', context)


@login_required(login_url='login')
def delete_skill(request, pk):
    skill = get_object_or_404(Skill, pk=pk)

    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill deleted successfully')
        return redirect('user_account')
    
    context = {'object': skill}
    return render(request, 'delete_template.html', context)

@login_required(login_url='login')
def inbox(request):
    profile = request.user.profile
    messageRequests = profile.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    context = {'messageRequests': messageRequests, 'unreadCount': unreadCount}
    return render(request, 'ulist_user/inbox.html', context)

@login_required(login_url='login')
def view_message(request, pk):
    profile = request.user.profile
    message = profile.messages.get(id = pk)
    if message.is_read == False:
        message.is_read = True
        message.save()
    context = {'message': message, 'profile': profile}
    return render(request, 'ulist_user/message.html', context)

def createMessage(request, pk):
    recipient = Profile.objects.get(id=pk)
    form = MessageForm()
    try:
        sender = request.user.profile
    except:
        sender = None
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient
            if sender:
                message.name = sender.name
                message.email = sender.email
            message.save()
            messages.success(request, 'Message sent successfully')
            return redirect('profiles-detail', pk = recipient.pk)
        else:
            messages.error(request, 'There was an error with your message')
    context = {'recipient': recipient, 'form': form}
    return render(request, 'ulist_user/message_form.html', context)