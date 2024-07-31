from django.db.models import Q
from .models import Profile,Skill
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def search_profile(request):
    search_query = ''
    if 'query' in request.GET:
        search_query = request.GET['query']
    
    skills = Skill.objects.filter(name__icontains = search_query)
    profiles = Profile.objects.distinct().filter(Q(name__icontains=search_query) | Q(short_info__icontains=search_query) | Q(skills__in=skills))

    return profiles, search_query

def paginateprofiles(request, profiles):
    # Pagination
    profiles = profiles.order_by('name')
    page = request.GET.get('page')
    results = 3
    paginator = Paginator(profiles, results)  # Show 10 projects per page
    
    try:
        profiles = paginator.page(page) 
    except PageNotAnInteger:
        page = 1 
        profiles = paginator.page(page) 
    except EmptyPage:
        page = paginator.num_pages  # If page is not an integer, deliver last page
        profiles = paginator.page(page)
    
    return profiles, paginator