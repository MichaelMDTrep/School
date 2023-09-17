from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from curriculum.models import CourseCompleted

# Create your views here.

@login_required
def users(request):

    if request.user.is_superuser:

        query = None

        if request.method == "POST":
            if 'query' in request.POST:
                query = request.POST['query']
                queries = Q(username__icontains=query)
                users = User.objects.filter(queries).order_by('-last_login')
        else:
            users = User.objects.all().order_by('-last_login')

        context = {
            'page': 'userdata',
            'users': users,
            'title': 'Users',
            'query': query,
        }

        return render(request, 'userdata/users.html', context)
    else:
        messages.warning(request, 'You do not have permission to access this page.')
        return redirect('home')
    

@login_required
def user(request, username):

    if request.user.is_superuser:
        
        user = get_object_or_404(User, username=username)
        course_completed = CourseCompleted.objects.filter(user=user).order_by('-date')

        context = {
            'page': 'userdata',
            'user': user,
            'course_completed': course_completed,
            'title': f'{username}',
        }

        return render(request, 'userdata/user.html', context)
    else:
        messages.warning(request, 'You do not have permission to access this page.')
        return redirect('home')