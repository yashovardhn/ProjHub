from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Project, Profile, Tag, Review
from .forms import ProjectForm, ReviewForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from .utils import search_project, paginateprojects




def project_list(request):
    projects, search_query = search_project(request)

    project, paginator = paginateprojects(request,projects)

    profiles = Profile.objects.all()
    context = {
        'project': project,    
        'search_query': search_query,
        'profiles': profiles,
        'paginator': paginator
    }
    
    return render(request, 'ulist/project.html', context)


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    reviews = Review.objects.filter(project=project)
    tags = project.tag.all()
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.project = project
            review.owner = request.user.profile  # Assuming user has a profile attribute
            review.save()
            messages.success(request, 'review submitted successfully')
            project.get_vote_count
            return redirect('project_detail', pk=project.id)
    else:
        form = ReviewForm()

    context = {
        'project': project,
        'tags': tags,
        'reviews': reviews,
        'form': form,
    }
    return render(request, 'ulist/project_file.html', context)


@login_required
@require_http_methods(["GET", "POST"])
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            # Retrieve the Profile instance related to the current user
            profile = get_object_or_404(Profile, user=request.user)
            project.owner = profile  # Assign the Profile instance
            project.save()
            messages.success(request, 'Project created successfully')
            return redirect('user_account')  # Adjust the redirect as needed
        else:
            messages.error(request, 'There was an error creating the project')
    else:
        form = ProjectForm()
    return render(request, 'ulist/project_form.html', {'form': form})

@login_required
@require_http_methods(["GET", "POST"])
def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully')
            return redirect('project')  # Adjust the redirect as needed
        else:
            messages.error(request, 'There was an error updating the project')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'ulist/project_form.html', {'form': form})

@login_required
@require_http_methods(["GET", "POST"])
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted successfully')
        return redirect('project')
    
    context = {'project': project}
    return render(request, 'delete_template.html', context)
