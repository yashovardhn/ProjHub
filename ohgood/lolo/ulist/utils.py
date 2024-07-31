from django.db.models import Q
from .models import Project,Tag,Review
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def search_project(request):
    search_query = ''
    if 'query' in request.GET:
        search_query = request.GET['query']
    
    tags = Tag.objects.filter(name__icontains=search_query)  # Use `tags` instead of `tag`
    projects = Project.objects.filter(
        Q(title__icontains=search_query) | 
        Q(description__icontains=search_query) | 
        Q(owner__name__icontains=search_query) |
        Q(tag__in= tags)  # Adjust the filter if needed
    ).distinct()
    return projects, search_query

def paginateprojects(request, projects):
    # Pagination
    page = request.GET.get('page', 1)
    results = 3
    paginator = Paginator(projects, results)  # Show 10 projects per page
    
    try:
        project = paginator.page(page) 
    except PageNotAnInteger:
        page = 1 
        project = paginator.page(page) 
    except EmptyPage:
        page = paginator.num_pages  # If page is not an integer, deliver last page
        project = paginator.page(page)
    
    return project, paginator