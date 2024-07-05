
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('', views.home, name='home'),
     path('allCourses/', views.all_courses, name='allCourses'),
     path('course/<str:pk>/', views.course, name='course'),
     path('courseDetail/<str:pk>/', views.course_detail, name='courseDetail'),
     path('addCourse/', views.add_course, name='addCourse'),
     path('editCourse/<str:pk>/', views.edit_course, name='editCourse'),
     path('myCourses/', views.my_courses, name='myCourses'),
     path('myAccount/<str:pk>/', views.my_account, name='myAccount'),

     path('addReference/', views.add_reference, name='addReference'),
     path('addModule/', views.add_module, name='addModule'),
     path('addContent/', views.add_content, name='addContent'),

     path('about/', views.about, name='about'),
     path('contact/', views.contact, name='contact'),

     path('accounts/', include('registration.backends.default.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
