from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from curriculum.models import CourseCompleted, CourseCategory
from django.utils.timezone import localdate

# Create your views here.

@login_required
def home(request):

    completed_courses = CourseCompleted.objects.filter(user=request.user)
    categories = CourseCategory.objects.all()

    goals = []
    stars = []

    for category in categories:
        for completed_course in completed_courses:
            if completed_course.date == localdate() and completed_course.course.category.id == category.id:
                goals.append((category.id, 1))
                break
        else:
            goals.append((category.id, 0))

    for category in categories:
        count = 0
        for completed_course in completed_courses:
            if completed_course.course.category.id == category.id:
                count += 1
        stars.append((category.id, count))

    context = {
        'page': 'home',
        'categories': categories,
        'goals': goals,
        'stars': stars,
        'title': 'Home',
    }

    return render(request, 'home/home.html', context)

