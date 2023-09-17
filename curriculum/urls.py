from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.curriculum, name='curriculum'),
    path('<int:course_id>/', views.course, name='course'),
    path('add-link/<int:course_id>/', views.add_course_link, name='add_course_link'),
    path('users/', include('django.contrib.auth.urls')),
    path(r'^curriculum/(?P<course_id>\d+)/$',views.passcoursetocurriculum, name='passcoursetocurriculum'), 

]