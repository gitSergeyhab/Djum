from django.contrib.auth.views import LogoutView
from django.urls import path
from job.views import MainView, ListVacanciesView, CardCompanyView, ListVacSpecialtiesView, CompaniesView, \
    OneVacancyView, CreateApplicationView, MySignupView, MyLogin, MyVacanciesView, UpdateCompanyView, \
    AddCompanyView, UserProfileView, DemoCompView, DemoResumeView, AddVacancyView, UpdateVacancyView, \
    SearcherView, AddUserResumeView, UpdUserResumeView, SentView, About

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('vacancies/', ListVacanciesView.as_view(), name='vacancies'),
    path('company/', CompaniesView.as_view(), name='companies'),
    path('companies/<int:pk>/', CardCompanyView.as_view(), name='company'),
    path('vacancies/cat/<str:slug>/', ListVacSpecialtiesView.as_view(), name='specialties'),
    path('vacancies/<int:pk>/', OneVacancyView.as_view(), name='vacancy'),
    path('vacancies/<int:pk>/send/', CreateApplicationView.as_view(), name='application'),
    path('addmycompany/', AddCompanyView.as_view(), name='addmycompany'),
    path('mycompany/<int:pk>', UpdateCompanyView.as_view(), name='update_comp'),
    path('mycompany/vacancies/', MyVacanciesView.as_view(), name='myvacancies'),
    path('profile/<int:pk>', UserProfileView.as_view(), name='profile'),
    path('demo_comp/', DemoCompView.as_view(), name='demo_comp'),
    path('demo_resume/', DemoResumeView.as_view(), name='demo_resume'),
    path('mycompany/vacancies/add/', AddVacancyView.as_view(), name='add_vac'),
    path('mycompany/vacancies/<int:pk>', UpdateVacancyView.as_view(), name='update_vac'),
    path('search/', SearcherView.as_view(), name='searcher'),
    path('myresume/', AddUserResumeView.as_view(), name='myresume'),
    path('myresume/<int:pk>', UpdUserResumeView.as_view(), name='updresume'),
    path('<int:pk>/sent/', SentView.as_view(), name='sent'),
    path('about/', About.as_view(), name='about'),
]

urlpatterns += [
    path('login', MyLogin.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('signup', MySignupView.as_view(), name='signup'),
]
