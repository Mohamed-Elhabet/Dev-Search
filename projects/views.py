from django.shortcuts import render , redirect 
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from projects.forms import ProjectForm , ReviewForm
from .models import Project , Tag
from django.db.models import Q 
from .utils import searchProjects , paginateProjects
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
from django.contrib import messages

# projectsList = [
#     {
#         'id':'1' ,
#         'title':'Ecommerce website' ,
#         'description':'Fully functional ecommerce website'
#     },
#     {
#         'id':'2',
#         'title':'portfolio website' , 
#         'description':'This was a project where i built out my portfolio'
#     } ,
#     {
#         'id':'3',
#         'title':'Social Network' , 
#         'description' :'Awesome oprn source project i am still working'
#     }
# ]

def projects(request):
    #return HttpResponse('Here are our products ')
    #return render(request , 'projects.html')
    
    # page = 'projects '
    # number = 10
    # context = {'page':page , 'number':number , 'projects':projectsList}

    # search_query =''
    # if request.GET.get('search_query'):
    #     search_query = request.GET.get('search_query')
    
    # tags = Tag.objects.filter(name__icontains =search_query)

    # projects = Project.objects.distinct().filter(
    #     Q(title__icontains = search_query) | 
    #     Q(description__icontains = search_query ) |
    #     Q(owner__name__icontains = search_query) |
    #     Q(tags__in = tags)
    # )

    projects , search_query = searchProjects(request)
    #projects = Project.objects.all()
    #page = 1
    # page = request.GET.get('page')
    # results = 3
    # paginator = Paginator(projects , results)

    # try:
    #     projects = paginator.page(page)
    # except PageNotAnInteger:
    #     page = 1
    #     projects = paginator.page(page)
    # except EmptyPage:
    #     page = paginator.num_pages
    #     projects = paginator.page(page)

    # leftIndex = (int(page)-4)
    # if leftIndex <1:
    #     leftIndex = 1
    
    # rightIndex = (int(page) +5)
    # if rightIndex > paginator.num_pages:
    #     rightIndex = paginator.num_pages +1
    
    # custom_range = range(leftIndex , rightIndex)
    custom_range , projects = paginateProjects(request , projects , 6)

    context = {'projects' :projects , 'search_query':search_query ,
               'custom_range':custom_range}
    return render(request , 'projects/projects2.html' ,context)

def project(request , pk):

    #return HttpResponse('single project' +" " +str(pk))
    #return render(request , 'single-project.html')

    # projectObj = None
    # for i in projectsList:
    #     if i['id'] == pk:
    #         projectObj = i
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    form = ReviewForm()

    # save vote for project
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        review.save()
        # update project votecount
        projectObj.getVoteCount # run as decorator

        messages.success(request , 'Your review was successfully submitted')
        return redirect('project', pk=projectObj.id)

    return render(request ,'projects/single-project2.html',{'project':projectObj , 'form':form})


@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form = ProjectForm
    
    if request.method == 'POST':
        #print(request.POST)
        form = ProjectForm(request.POST , request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile 
            project.save()
            return redirect('account')

    context = {'form' : form}
    return render(request , 'projects/project_form.html',context)


@login_required(login_url="login") 
def updateProject(request , pk):
    profile = request.user.profile
    #project = Project.objects.get(id=pk)
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST ,request.FILES , instance=project)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {'form':form}
    return render(request , 'projects/project_form.html' , context)

@login_required(login_url="login") 
def deleteProject(request , pk):
    profile = request.user.profile
    #project = Project.objects.get(id=pk)
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context={'object' : project}
    return render(request , 'delete_template.html',context)





