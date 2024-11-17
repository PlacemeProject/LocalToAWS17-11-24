from django.urls import path,include
from . import views

app_name = 'job_seeker'

urlpatterns = [
    path('', views.Home,name='home'),
    path('profile/',views.Profile,name='profile'),
    path('notifications/',views.Notifications,name='notifications'),
    path('create-profile/',views.CreateProfile,name='create-profile'),
    path('search/',views.Search,name='search'),
    path('job/',views.Job,name='job'),
    path('my-job/',views.MyJob,name='my-job'),
    path('apply/',views.Apply,name='apply'),
    path('status/',views.Status,name='status'),
    path('onboarding/',views.Onboarding,name='onboarding'),

]
