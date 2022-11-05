from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import include
from MyApps1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    path('java/', views.java_exams_view),
    path('python/', views.python_exams_view),
    path('aptitude/', views.aptitude_exams_view),
    path('logout/', views.logout_view),

    path('signup/',views.signup_view),


    re_path('^$', views.home_page_view), #dont use re_path() for def/any-url
]

